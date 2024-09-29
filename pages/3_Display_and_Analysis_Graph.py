import pandas as pd
import networkx as nx 
import streamlit as st
import matplotlib.pyplot as plt 
from typing import Dict, Any
from src.info2json import load_graph, get_dict_info, load_tokens
from src.utils import (
  convert_graph_info_to_dataframe,
  info_of_metadata_to_dataframe,
  get_metadatas,
  pagerank
)

#* Page-Configuration
st.set_page_config(
  page_title='Display and Analysis Graph',
  layout='wide'
)

#* Title
st.title ('Visualización y Análisis del Grafo')

G:nx.Graph = load_graph ()
info:Dict = get_dict_info (G=G)
N:int = len(G.nodes)

with st.expander (label='**Información sobre los Diseños de Visualización**'):
  st.markdown ("""
  **Spring:** Este diseño es una implementación del algoritmo de fuerza de 
  atracción-repulsión de Fruchterman-Reingold. Se caracteriza este diseño por:
  
  - Simplicidad visual
  - Distribución equilibrada
  - Menor número de colisiones

  **Circular:** Este tipo de diseño es particularmente útil cuando se quiere
  representar relaciones entre nodos de manera cíclica o simétrica. Se 
  caracteriza este diseño por:
    
  - Organización cíclica
  - Posicionamiento automático
  - Flexibilidad
  
  **Kamada-Kawai:** Se caracteriza:

  - *Aproximación geométrica*: intenta aproximar la geometría real de la red, 
  minimizando la energía potencial de repulsión entre nodos
  - *Algoritmo iterativo*: utiliza un algoritmo de optimización no lineal para 
  posicionar los nodos en un espacio bidimensional
  
  **Spiral:** Este diseño proporciona una forma elegante de organizar los nodos de 
  un grafo siguiendo un patrón en espiral.
  """)

dict_layouts:Dict[str,Any] = {
  'spring':       nx.spring_layout(G),
  'circular':     nx.circular_layout(G),
  'kamada-kawai': nx.kamada_kawai_layout(G),
  'spiral':       nx.spiral_layout(G),
}

layout = None
select_layout = st.selectbox(
  label='Selecciona un diseño para la visualización del grafo',
  options=dict_layouts.keys()
)
layout = dict_layouts[select_layout]

#* Dataframes para el analisis 
df = convert_graph_info_to_dataframe(G=G)
metadata = get_metadatas(G=G)
df_names = df[ ['name','degree'] ]
df_metadata = df.drop('degree',axis=1)
df_metadata_transform = info_of_metadata_to_dataframe(df=df, metadata_name=metadata)
tokens: Dict = { name:value for name,value in load_tokens().items() if name in metadata }

#* LAYOUT
if not layout == None:
  col1, col2 = st.columns([2,1])
  with col1:
    fig, ax = plt.subplots (figsize=(min(int(N*0.9),30),min(int(N*0.9),30)))
    nx.draw (
      G=G,
      pos=layout,

      with_labels=True,
      ax=ax
    )
    st.pyplot(fig=fig)
  with col2:
    st.write ('### Nombres de los Vértices')
    st.write (df_names)

st.write ('### Características del grafo')
density = nx.density (G=G)

diameter = ''
periphery = ''
try:
  diameter = nx.diameter (G=G)
  periphery = nx.periphery (G=G)
except nx.NetworkXError:
  diameter = 'el grafo no es conexo. No se puede calcular el diámetro'
  periphery = 'el grafo no es conexo'

ave_degree = sum(dict(G.degree()).values()) / len(G.nodes())
ave_clustering = nx.average_clustering (G=G)
ave_shortest_path = nx.average_shortest_path_length (G=G)
ave_neighbors_degree = nx.average_neighbor_degree (G=G)

centrality = {
  'closeness'   : nx.closeness_centrality (G=G),
  'betweenness' : nx.betweenness_centrality (G=G),
  'degree'      : nx.degree_centrality (G=G),
  'eigenvector' : nx.eigenvector_centrality (G=G)
}

st.markdown (f"""
**Densidad**: {density:.2f}

**Camino característico**: {ave_shortest_path:.2f}

**Diámetro**: {diameter}

**Periferia**: {periphery}

**Grado medio**: {ave_degree:.2f}

**Valor promedio de clustering**: {ave_clustering:.2f}

""")

col4_1, col4_2, col4_3, col4_4 = st.columns ([1,1,1,1])
with col4_1:
  st.write ('**Closeness Centrality**')
  for n, v in sorted( centrality['closeness'].items(), key=lambda x : x[1], reverse=True ):
    st.write (f"- Node {n}: {v:.2f}")
with col4_2:
  st.write ('**Betweenness Centrality**')
  for n, v in sorted( centrality['betweenness'].items(), key=lambda x : x[1], reverse=True ):
    st.write (f"- Node {n}: {v:.2f}")
with col4_3:
  st.write ('**Degree Centrality**')
  for n, v in sorted( centrality['degree'].items(), key=lambda x : x[1], reverse=True ):
    st.write (f"- Node {n}: {v:.2f}")
with col4_4:
  st.write ('**Eigenvector Centrality**')
  for n, v in sorted( centrality['eigenvector'].items(), key=lambda x : x[1], reverse=True ):
    st.write (f"- Node {n}: {v:.2f}")

st.write ('PakeRank')
# TODO: Falta PageRank

with st.expander ('Información sobre las características del grafo'):
  st.markdown("""
  La información que nos brinda estas características pueden ser tomadas en cuenta para la simulación
  
  **Densidad**: 
    Un valor cercano a 0 indica que el grafo está débilmente conectado (pocas aristas en relación al número de nodos).
    Un valor cercano a 1 indica que el grafo está muy conectado y denso.
    En las redes sociales, un alto valor podría indicar una comunidad muy unida y cohesionada, 
    mientras que un bajo valor podría indicar una comunidad fragmentada o dispersa.

  **Camino característico**:
    Mide el grado de separación de los nodos. Un valor pequeño indica que los nodos están separados
    cerca unos de otros, mientras que un valor grande sugiere que hay una mayor separación entre los nodos
    
  **Diámetro**: 
    Es el máximo de las distancias entre cualesquiera par de nodos. 

  **Grado medio**: 
    Número de vecinos (conexiones a otros nodos) medio que tiene un grado. 

  **Centralidad**: 
    Permite realizar un análisis para indicar aquellos nodos que poseen una mayor cantidad
    de relaciones y por ende, los influyentes dentro del grupo. 

  **Valor promedio de clustering**: 
    Es una métrica que permite medir la propensión de los nodos a agruparse en subgrafos densos 
    dentro del grafo general. En otras palabras, indica cuánto se parecen los vecinos cercanos 
    entre sí
  """)

if len(metadata) > 1:
  st.write ('### Dataframes sobre Metadatos')

  st.write ('El siguiente dataframe muestra la información que almacena cada vértice (persona) en el grafo')
  st.write (df_metadata)

  st.write ('El siguiente dataframe es otra forma para mostrar la información de cada persona, esta vez por cada valor de la lista de metadatos se le asigna una columna del dataframe')
  st.write (df_metadata_transform)

  with st.expander ('**Posibles valores que puede recibir cada metadato**'):
    for name, token_list in tokens.items():
      st.markdown (f'{name.upper()} : {', '.join(token_list)}')

  metadata.remove('name')
  df_counter = df
  for m in metadata:
    counter = df_metadata[m].apply ( lambda row: len( row ) )
    df_counter[m] = counter

  st.write ('Ahora se realiza un conteo de valores en cada metadato')
  st.write (df_counter)

  df_counter_ind = {name : { m:df_metadata_transform[m].value_counts()[1] for m in value } for name, value in tokens.items() } 
  dict_df_counter_ind:Dict[str,pd.DataFrame] = { }
  for m in metadata:
    dict_df_counter_ind[m] = pd.DataFrame({
      m       : df_counter_ind[m].keys(),
      'count' : df_counter_ind[m].values()
    })

  st.write ('Ahora se realiza un conteo para saber la cantidad de personas que le gusta el metadato X')
  for m in metadata:
    st.write (f'**Conteo para el metadato**: {m.upper()}')
    col3_1, col3_2 = st.columns( [1,2] )
    with col3_1:
      st.write (dict_df_counter_ind[m])
    with col3_2:
      # TODO: Mejorar lo siguiente 
      st.write (f'**Mayor valor**: {dict_df_counter_ind[m].max()}')
      st.write (f'**Menor valor**: {dict_df_counter_ind[m].min()}')
      # TODO: usar matplotlib para graficar este dataframe
