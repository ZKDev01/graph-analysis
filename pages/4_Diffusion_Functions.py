import copy 
import random 
import networkx as nx
import streamlit as st 
from typing import Dict, List, Set, Any
from src.graph import get_dict_info
from src.info2json import load_graph, save_f_diffusion, load_f_diffusion 
from src.generators import generate_f_diffusion, generate_int
from src.f_diffusion import (
  Base_DiffusionFunction,
  Probabilistic_DiffusionFunction,
  Population_DiffusionFunction
)
# Page-Configuration
st.set_page_config(
  page_title='Diffusion Functions',
  layout='wide'
)

G:nx.Graph = load_graph()
N:int = len(G.nodes())
info = get_dict_info(G=G)
neighbors = info['neighbors']

st.title ('Generación de Funciones de Difusión')

with st.expander ('**About**'):
  markdown = """ 
  Las posibles funciones de difusión son:
  - *Base*: El nodo que tenga asignado esta función siempre difundirá la información a sus nodos vecinos
  - *Probabilistic*: El nodo difundirá la información según un valor de probabilidad `p`
  """
  st.markdown (markdown)

options = {
  'Base'          : Base_DiffusionFunction(G=G),
  'Probabilistic' : Probabilistic_DiffusionFunction(G=G),
  'Population'    : Population_DiffusionFunction(G=G)
}
selection = st.multiselect (
  label='Selecciona los tipos de funciones de difusión para los vértices',
  options=options.keys()
)

btn_generate = st.button ('Generar')
btn_show = st.button ('Mostrar')

if btn_generate and len(selection) > 0:
  # generar random los int
  list_random : List[int] = generate_int(N=len(G.nodes),M=len(selection)-1)
  
  # mapear los datos segun la entrada
  mapper_options: Dict[ int,Base_DiffusionFunction ] = { i:copy.deepcopy(options[name]) for i,name in enumerate(selection) } 
  list_mapper : Dict[ int,Base_DiffusionFunction ] = { i:copy.deepcopy(mapper_options[value]) for i,value in enumerate(list_random) }
  
  for i,f in list_mapper.items():
    if isinstance(f,Probabilistic_DiffusionFunction):
      f.set_config( i=i, p=random.random() )
    elif isinstance(f,Population_DiffusionFunction):
      f.set_config( i=i, degree=random.randint(a=1,b=N-1), neighbors=neighbors )
    
    else: f.set_config( i=i )

  #st.write (list_mapper)

  save_f_diffusion (f_diffusion=list_mapper)
  f_diffusion = load_f_diffusion (G=G, info=info)
  st.write (f_diffusion)

if btn_show:
  f_diffusion = load_f_diffusion (G=G, info=info)
  st.write (f_diffusion)  
