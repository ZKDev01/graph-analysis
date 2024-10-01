import networkx as nx
import streamlit as st
from typing import Dict, List, Any, Set
from src.info2json import load_graph, load_f_diffusion
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

- *Tiempo promedio de propagación*: Calcula cuánto tiempo tardó 
en propagarse desde el nodo inicial hasta todos los demás nodos
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
f_diffusion:Dict[ int,Base_DiffusionFunction ] = load_f_diffusion( G=G )
simulator = InformationDiffusion_Simulator( G=G )
n_nodes = [ i for i in range(len(G.nodes())) ]

st.title ("Simulación")

with st.expander ('**About**'):
  st.markdown (markdown)

n_step = st.number_input ('Seleccione la cantidad de pasos de simulación', min_value=1, max_value=10)
roots = st.multiselect ('Selecciona los nodos iniciales para propagar la información', n_nodes)

btn_start = st.button ('Simular')

if btn_start and len(roots) > 0:
  log = simulator.simulate(
    f_diffusion=f_diffusion,
    root=roots,
    STEP=n_step
  )

  st.write (log)
