import streamlit as st 

from src.data_faker import (
  generate_diffusion_function
)
from src.graph import (
  DynamicGraph,
  Vertex
)
from src.info2json import (
  load_edges,
  load_vertex,
  save_diffusion_functions,
  load_diffusion_functions
)

st.write ( 'Es posible generar funciones de difusion usando un tipo en especifico para todo los vertices:' )

btn_generate = st.button ( "Generar funciones de difusion 'Base'" )
btn_load = st.button ( "Cargar funciones de difusion" )

edges = load_edges ( )
vertex = load_vertex ( )

graph = DynamicGraph ( vertex=vertex )
graph.set_adj_list ( edges )

if btn_generate:
  
  
  diffusion_functions = generate_diffusion_function ( graph=graph )
  save_diffusion_functions ( input=diffusion_functions )

if btn_load: 
  output = load_diffusion_functions ( graph=graph )
  st.write ( output )

# CHECK que len(diffusion-functions) == len(vertex of dynamic graph)

# mostrar
