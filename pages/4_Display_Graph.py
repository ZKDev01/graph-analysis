import streamlit as st 
import networkx as nx 
import pandas as pd 
import matplotlib.pyplot as plt 

from typing import Dict, List, Any, Set, Tuple

from src.info2json import (
  load_edges,
  load_vertex
)

from src.graph import (
  Vertex,
  DynamicGraph
)

st.title ( "Display Graph" )

G = nx.Graph ( )


st.markdown ( """
Graph Analysis
- Clustering
- Centralidad
""" )

def convert_edges_from_dynamic_graph ( adj_list: Dict[ int, List[int] ] ) -> List:
  output: List = [ ]
  for i, list_i in adj_list.items ( ):
    for j in list_i:
      if not (j,i) in output:
        output.append ( (i,j) )
  return output


vertex : List[ Vertex ] = load_vertex ( )
edges : Dict[ int, List[ int ] ] = load_edges ( )

dynamic_graph = DynamicGraph ( vertex=vertex )
dynamic_graph.set_adj_list ( edges )

G.add_nodes_from( [ key for key, _ in dynamic_graph.vertex.items ( ) ] )
G.add_edges_from( convert_edges_from_dynamic_graph ( dynamic_graph.adj_list ) )

fig, ax = plt.subplots(figsize=(3, 2))
nx.draw(G, with_labels=True, ax=ax)
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])

st.pyplot ( fig=fig )
