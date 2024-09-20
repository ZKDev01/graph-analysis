import streamlit as st 

from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

from src.graph import (
  Vertex,
  Metadata,
  DynamicGraph
)
from src.info2json import (
  load_vertex
)
from src.random_models import (
  model_ER
)


def display_dynamic_graph (  ) -> None:
  #vertex = load_vertex ( )
  #graph = DynamicGraph ( vertex=vertex )
  # graph.adj_list = [ ]
  #graph = model_ER ( graph=graph, p = 0.5 )

  elements = {
    "nodes" : [
    
      { "data": { "id": 1, "label": "Person", "name": "Person01", "preferences": ['rock'] } },
      { "data": { "id": 2, "label": "Person", "name": "Person02", "preferences": ['rock'] } },
      { "data": { "id": 3, "label": "Person", "name": "Person03", "preferences": ['rock'] } },
      { "data": { "id": 4, "label": "Person", "name": "Person04", "preferences": ['rock'] } },
      { "data": { "id": 5, "label": "Person", "name": "Person05", "preferences": ['rock'] } }
    
    ],
    "edges" : [
      
      { "data": { "id": 11, "label": "Link", "source": 1, "target": 2 } },
      { "data": { "id": 12, "label": "Link", "source": 1, "target": 3 } },
      { "data": { "id": 13, "label": "Link", "source": 2, "target": 3 } },
      { "data": { "id": 14, "label": "Link", "source": 2, "target": 4 } },
      { "data": { "id": 15, "label": "Link", "source": 2, "target": 5 } }
    
    ]
  }

  node_style = [
    NodeStyle ( "Person", '#FF7F3E', "name", "person" )
  ]
  edge_style = [
    EdgeStyle ( "Link", "#2A629A", "content", "description" )
  ]

  st_link_analysis ( 
    elements=elements,
    layout='cose',
    node_styles=node_style,
    edge_styles=edge_style
  )

display_dynamic_graph ( )



# TODO: mostrar el grafo generado con los parametros anteriormente

