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
  model_ER
)
from src.info2json import (
  load_vertex,
  save_edges,
  load_edges
)
from src.utils import (
  convert_adj_list_to_d2array 
)



def show_heatmap ( matrix: np.matrix ) -> None:
  fig, ax = plt.subplots ( figsize = (10,8) )
  heatmap = sns.heatmap ( matrix, annot=True, cmap="YlGnBu", fmt='.0f',
    xticklabels= [ f"Vertex { i }" for i in range ( len(matrix) ) ],
    yticklabels= [ f"Vertex { i }" for i in range ( len(matrix) ) ]
    )
  plt.title( 'Matrix de Adyacencia' )
  plt.xlabel ( 'Vertex' )
  plt.ylabel ( 'Vertex' )
  plt.tight_layout ( )
  st.pyplot ( fig=fig )



models = [ 'Erdos-Renyi Model' ]
select = st.selectbox ( label='Select a model', options=models )

btn_model = st.button ( 'Generate Edges' )
btn_load_edges = st.button ( 'Load Edges' )

if btn_model and select == 'Erdos-Renyi Model': 
  vertex = load_vertex ( )
  graph = DynamicGraph ( vertex=vertex )
  graph = model_ER ( graph=graph, p = 0.5 )
  
  save_edges ( graph.adj_list )
  # adj_matrix = convert_adj_list_to_d2array ( graph.adj_list )
  st.write ( graph.adj_list )

if btn_load_edges:
  adj_list = load_edges ( )
  st.write ( adj_list )
