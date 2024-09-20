import streamlit as st 

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
  load_vertex
)

models = [ 'Erdos-Renyi Model' ]
select = st.selectbox ( label='Select a model', options=models )

btn_model = st.button ( 'Generate Edges' )


if btn_model and select == 'Erdos-Renyi Model': 
  vertex = load_vertex ( )
  graph = DynamicGraph ( vertex=vertex )
  graph = model_ER ( graph=graph, p = 0.5 )
  st.write ( graph )



# TODO: salvar las aristas
# TODO: load las aristas
# TODO: mostrar las aristas like a adj_matrix
