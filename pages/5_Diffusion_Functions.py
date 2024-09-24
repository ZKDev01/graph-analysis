import streamlit as st 

from src.diffusion_functions import (
  generate_diffusion_function
)
from src.graph import (
  DynamicGraph,
  Vertex
)
from src.info2json import (
  load_edges,
  load_vertex
)

st.write ( 'Es posible generar funciones de difusion usando un tipo en especifico para todo los vertices:' )

btn_generate = st.button ( "Generar funciones de difusion 'Base'" )

if btn_generate:
  edges = load_edges ( )
  vertex = load_vertex ( )
  graph = DynamicGraph ( vertex=vertex )
  graph.set_adj_list ( edges )
  diffusion_functions = generate_diffusion_function ( graph=graph )
  for i, f_d in diffusion_functions.items ( ):
    st.write ( i )
    st.write ( f_d )



# CHECK que len(diffusion-functions) == len(vertex of dynamic graph)

# mostrar
