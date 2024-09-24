import numpy as np
import seaborn as sns
import streamlit as st 
import matplotlib.pyplot as plt

from typing import Dict, List, Any, Set

from src.graph import (
  Vertex, 
  Metadata, 
  DynamicGraph
)
from src.random_models import (
  model_ER,
  model_WS,
  model_BA
)
from src.info2json import (
  load_vertex,
  save_edges,
  load_edges
)
from src.utils import (
  convert_adj_list_to_d2array 
)

# Config params
models = [ 'Erdos-Renyi Model', 'Watts-Strogatz Model', 'Barabasi-Albert Model' ]
select = st.selectbox ( label='Select a model', options=models )

p = st.number_input ( 'Model Erdos-Renyi => P', min_value=0.0, max_value=1.0, value=0.5 )

# Buttons
btn_model = st.button ( 'Generate Edges' )
btn_load_edges = st.button ( 'Load Edges' )

# Generate Edges
vertex = load_vertex ( )
graph = DynamicGraph ( vertex=vertex )

if btn_model and select == 'Erdos-Renyi Model': 
  graph = model_ER ( graph=graph, p = p )
  save_edges ( graph.adj_list )
  st.write ( graph.adj_list )

if btn_model and select == 'Watts-Strogatz Model':
  st.write ( 'falta' )

if btn_model and select == 'Barabasi-Albert Model':
  st.write ( 'falta' )


# Load Edges from JSON
if btn_load_edges:
  adj_list = load_edges ( )
  st.write ( adj_list )
