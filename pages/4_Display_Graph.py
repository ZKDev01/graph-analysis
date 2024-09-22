import streamlit as st 

from typing import Dict, List, Any, Set
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

from src.graph import (
  Vertex,
  Metadata,
  DynamicGraph
)
from src.info2json import (
  load_vertex,
  load_edges
)
from src.random_models import (
  model_ER
)

def convert_node_in_data ( key: int, v: Vertex ) -> Dict:
  data: Dict = { }
  data[ "id" ] = key
  data[ "label" ] = "Person"
  data[ "name" ] = v.name
  for m in v.metadatas:
    data[ f"metadata: {m.name}" ] = m.value
  return data

def eliminate_symmetric_edges( adj_list: Dict[ int, List[ int ] ] ) -> Any:
  edges: List = [ ]
  for i, l in adj_list.items ( ):
    for j in l:
      if (j,i) not in edges:
        edges.append ( (i,j) )
  return edges


def convert_adj_list_in_data ( N: int, adj_list: Dict[ int, List[ int ] ] ) -> Dict:
  data: List[ Dict ] = [ ]
  counter = 0
  l = eliminate_symmetric_edges ( adj_list=adj_list )
  for pair in l:
    d: Dict = { }
    d[ "id" ] = N + counter
    d[ "label" ] = "Link"
    d[ "source" ] = pair[0]
    d[ "target" ] = pair[1]
    counter+=1
    data.append ( { "data" : d } )
  return data

def display_dynamic_graph (  ) -> None:
  vertex = load_vertex ( ) 
  edges = load_edges ( )
  
  graph = DynamicGraph ( vertex=vertex )
  
  vertex: Dict[ int, Vertex ] = graph.vertex
  graph.set_adj_list ( edges )

  N = len ( vertex.keys ( ) ) 
  

  elements = {
    "nodes" : [ { "data": convert_node_in_data(key=key,v=v) } for key, v in vertex.items ( ) ],
    "edges" : convert_adj_list_in_data ( N=N, adj_list=edges )
  }

  node_style = [
    NodeStyle ( label="Person", color='#FF7F3E', caption="name", icon="person" )
  ]
  edge_style = [
    EdgeStyle ( label="Link", color="#2A629A", directed=False, labeled=False )
  ]

  st_link_analysis ( 
    elements=elements,
    layout='circle',
    node_styles=node_style,
    edge_styles=edge_style
  )
  

display_dynamic_graph ( )



# TODO: mostrar el grafo generado con los parametros anteriormente

