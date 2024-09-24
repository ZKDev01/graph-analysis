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
from src.utils import (
  convert_edges_from_dynamic_graph
)

# Create Graph
G = nx.Graph ( )

vertex : List[ Vertex ] = load_vertex ( )
edges : Dict[ int, List[ int ] ] = load_edges ( )

dynamic_graph = DynamicGraph ( vertex=vertex )
dynamic_graph.set_adj_list ( edges )

G.add_nodes_from( [ key for key, _ in dynamic_graph.vertex.items ( ) ] )
G.add_edges_from( convert_edges_from_dynamic_graph ( dynamic_graph.adj_list ) )

# Streamlit Display
st.title ( "Display Graph" )

## Layout for Display Graph
layout_options = {
  'spring' : nx.spring_layout( G ),
  'circular' : nx.circular_layout ( G ),
  'random' : nx.random_layout ( G )
}
layout_select = st.selectbox ( label='Select Layout', options=layout_options.keys( ) )
pos = layout_options[layout_select]

## Buttons
btn_display = st.button ( f'Display Graph with Layout {layout_select}' )

if btn_display:
  fig, ax = plt.subplots(figsize=(9, 9))
  nx.draw_networkx_nodes (
    G=G,
    pos=pos,
    ax=ax
  )
  nx.draw_networkx_edges(
    G=G,
    pos=pos,
    edgelist=G.edges,
    ax=ax
  )
  
  ax.set_xlim([1.2*x for x in ax.get_xlim()])
  ax.set_ylim([1.2*y for y in ax.get_ylim()])

  st.pyplot ( fig=fig )
