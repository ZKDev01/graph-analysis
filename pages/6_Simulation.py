import streamlit as st

from src.info2json import (
  load_diffusion_functions,
  load_edges,
  load_vertex
)
from src.simulation import (
  InformationDiffusion_Simulator
)
from src.graph import DynamicGraph

# Cargar el grafo y tener dos botones, cargar simulacion y ejecutar simulacion con N pasos

## select box para N pasos y boton y hay que guardar el log y 

## como analizar una simulacion?

# cargar todo

st.write ( 'This is for simulation' )

vertex = load_vertex ( )
edges = load_edges ( )
graph = DynamicGraph ( vertex=vertex )
graph.set_adj_list ( adj_list=edges )

diffusion_functions = load_diffusion_functions ( graph=graph )

simulator = InformationDiffusion_Simulator(graph=graph, root=0)
log = simulator.simulate ( diffusion_functions=diffusion_functions, step=10 )

st.write ( log )