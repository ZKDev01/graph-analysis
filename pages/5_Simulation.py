import pandas as pd
import networkx as nx
import streamlit as st
from typing import Dict, List, Any, Set
from src.utils import convert_graph_info_to_dataframe
from src.info2json import load_graph, load_f_diffusion, get_dict_info
from src.simulation import InformationDiffusion_Simulator
from src.f_diffusion import Base_DiffusionFunction

# Page-Configuration
st.set_page_config(
  page_title='Simulation',
  layout='wide'
)

markdown = """
Hacer una simulación en un grafo permite obtener una gran 
cantidad de información valiosa sobre el comportamiento del
mismo. 

**Métricas básicas**

- *Grado de conectividad*: Determina qué porcentaje de nodos 
recibieron la información durante la simulación
- *Velocidad de propagación*: Compara cómo cambia la velocidad 
de propagación a lo largo de los pasos

**Análisis de influencia**

- Algunos nodos con mayor conexión con otros tienden a distribuir
la información más rápido. Lo mismo con los nodos centrales, los 
cuales tienen a ser los más conectados y son los capaces de llevar 
la información al resto de nodos del grafo

**Estudio de patrones**
- *Patrones de propagación*: Busca patrones recurrentes en cómo
se distribuye la información a través del grafo
- *Isolados y grupos*: Nodos o subgrupos que no participaron en 
la propagación o que tuvieron un comportamiento diferente

**Análisis de vulnerabilidad**
- *Puntos débiles*: Localiza nodos críticos que si fueran 
eliminados podrían afectar la propagación
- *Redundancia*: Evalua cómo la red se comportaría si algunos 
nodos fallaran o fueran bloqueados 

**Análisis estadístico**
- *Distribución de tiempos*: Estudia cómo se reparte el tiempo
necesario para que cada nodo reciba la información
"""

G:nx.Graph = load_graph()
info:Dict = get_dict_info(G=G)
df = convert_graph_info_to_dataframe(G=G)
df = df[ ['name','degree'] ]
N:int = len(G.nodes())
f_diffusion:Dict[ int,Base_DiffusionFunction ] = load_f_diffusion( G=G, info=info )
simulator = InformationDiffusion_Simulator( G=G )
n_nodes = [ i for i in range(N) ]

st.title ("Simulación")

with st.expander ('**About**'):
  st.markdown (markdown)

n_step = st.number_input ('Seleccione la cantidad de pasos de simulación', min_value=1)
roots = st.multiselect ('Selecciona los nodos iniciales para propagar la información', n_nodes)

btn_start = st.button ('Simular')

if btn_start and len(roots) > 0:
  log = simulator.simulate(
    f_diffusion=f_diffusion,
    root=roots,
    STEP=n_step
  )
  df_log = pd.DataFrame ( 
    log
  ).T 
  st.write (df_log)
  analized = [ value['analized'] for _,value in log.items() ]
  analized_len = [ len(value) for value in analized ] 
  not_analized = [ i for i in range(N) if i not in analized[-1] ]

  st.write ('Nodos en los cuales no llegó la información')
  st.write ( not_analized )

  # Metricas basicas
  ## Grado de conectividad 
  st.write ( f'**Grado de conectividad**: {analized_len[-1] / N}' )
  
  ## Velocidad de propagación
  st.write ( '**Tiempo de propagación**' )
  st.bar_chart ( analized_len )

  # Analisis de Vulnerabilidad
  ## Nodos con degree bajo
  st.write ('Analizando los nodos con bajo grado')
  df_sorted = df.sort_values('degree', ascending=True)
  num_rows = int(len(df)*0.2)
  st.write ( df_sorted.head(num_rows) )

  ## Nodos con funcion de difusion 'complicada'
  st.write ('Nodos complicados por su función de difusión son los siguientes:')
  complicated:Dict[int,str] = {} 
  for i,f in f_diffusion.items():
    if not f.calification(): complicated[i] = f.__repr__()
  st.write (complicated)

