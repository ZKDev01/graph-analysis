import streamlit as st 
from typing import Dict, List, Set, Any
from src.graph import create_graph, get_dict_info
from src.info2json import load_tokens, save_graph, load_graph

# Page-Configuration
st.set_page_config(
  page_title='Graph Generation',
  layout='wide'
)

# Title
st.write ( "# Generación de Grafos" )

# Input Config
col1_1, col1_2 = st.columns([1,2])

with col1_1:
  ## Vertices del grafo
  N = st.number_input (
    label="Introduce la cantidad de vértices que desea generar para el grafo",
    min_value=1,
    max_value=1000,
    step=1
  )

with col1_2:
  ## Metadatos de los Vertices
  tokens = load_tokens()
  metadata_options = tokens.keys()
  metadata_select = st.multiselect ( 
    label='Selecciona los metadatos que desea que tengan los vértices del grafo',
    options=metadata_options 
  )  

## Modelo de Generacion Aleatoria de Aristas 
param_model: Dict = { }

with st.form ('barabasi-albert model'):
  param_model[ 'm' ] = st.number_input (
    label='Selecciona el valor $m$ del Modelo Barabasi-Albert',
    min_value=1
  )
  btn_model_ba = st.form_submit_button(
    label='Generar grafo con el Modelo Barabasi-Albert'
  )
  with st.expander (label='**Información sobre el Modelo Barabasi-Albert**'):
    st.markdown (
    """
    A un grafo, generado a partir de este modelo, se le añaden nodos cada uno con 
    $m$ aristas que se atan preferencialmente a nodos existentes con alto grado.

    Este sistema se conoce como conexión preferencial (preferential attachments) 
    y se puede explicar con la paradoja de 'the rich get richer'
    """)

with st.form ('watts-strogatz model'):
  col2_1, col2_2 = st.columns ([1,1])
  with col2_1:
    param_model[ 'k' ] = st.number_input (
      label='Selecciona el valor $k$ para el Modelo Watts-Strogatz',
      min_value=1 
    )
  with col2_2:
    param_model[ 'p' ] = st.number_input (
      label='Selecciona el valor $p$ para el Modelo Watts-Strogatz',
      min_value=0.0,
      max_value=1.0
    )
  btn_model_ws = st.form_submit_button(
    label='Generar grafo con el Modelo Watts-Strogatz'
  )
  with st.expander (label='**Información sobre el Modelo Watts-Strogatz**'):
    st.markdown (
    """
    Este modelo de red combina características de redes ordenadas y aleatorias, y es
    uno de los modelos que más se asemeja a las redes reales. 
    
    $k$: este parámetro indica cuántos vecinos cercanos de cada nodo están conectados 
    en una topología de anillo

    $p$: este parámetro representa la probabilidad de reentrelazar cada arista en el 
    proceso de creación del grafo

    **Nota**: Si $p$ se acerca a 0, el grafo tiende a ser completamente regular 
    (como un anillo). Cuando $p$ se acerca a 1, el grafo tiende a ser 
    completamente aleatorio (como una red binomial)
    """)


description = ""
name_model = "barabasi-albert" if btn_model_ba else "watts-strogatz"

if btn_model_ba:
  description = f"""
  **Modelo Seleccionado**: Barabasi-Albert

  Los parámetros para la generación del grafo son:
  - $N$: {N}
  - Metadatas: {', '.join(metadata_select)}
  - Parámetros del Modelo: 
    - $m$: {param_model['m']}
  """

if btn_model_ws:
  description = f"""
  **Modelo Seleccionado**: Watts-Strogatz

  Los parámetros para la generación del grafo son:
  - $N$: {N}
  - Metadatas: {', '.join(metadata_select)}
  - Parámetros del Modelo: 
    - $k$: {param_model['k']}
    - $p$: {param_model['p']}
  """

with st.expander ('**Posibles valores que puede recibir cada metadato**'):
  for name, token_list in tokens.items():
    st.markdown (f'{name.upper()} : {', '.join(token_list)}')

G = None
if btn_model_ws or btn_model_ba:
  st.write ('### Información sobre el grafo generado')
  st.markdown (description)
  tokens_for_graph = { key:value for key,value in tokens.items() if key in metadata_select }
  G = create_graph(
    N=N,
    metadatas=tokens_for_graph,
    model=name_model,
    param_model=param_model
  )
  save_graph(G=G)

