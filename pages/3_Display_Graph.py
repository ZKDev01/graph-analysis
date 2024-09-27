import networkx as nx 
import streamlit as st
import matplotlib.pyplot as plt 
from typing import Dict, Any 
from src.info2json import load_graph, get_dict_info

G:nx.Graph = load_graph ()
info:Dict = get_dict_info (G=G)

dict_layouts:Dict[str,Any] = {
  'spring':       nx.spring_layout(G),
  'circular':     nx.circular_layout(G),
  'kamada-kawai': nx.kamada_kawai_layout(G),
  'spiral':       nx.spiral_layout(G),
}

layout = None
select_layout = st.selectbox(
  label='Selecciona un layout para display el grafo',
  options=dict_layouts.keys()
)
layout = dict_layouts[select_layout]

if not layout == None:
  col1, col2 = st.columns([2,1])
  with col1:
    fig, ax = plt.subplots ()
    nx.draw_networkx_nodes(
      G=G,
      pos=layout,
      ax=ax
    )
    nx.draw_networkx_edges(
      G=G,
      pos=layout,
      edgelist=G.edges,
      ax=ax
    )
    st.pyplot(fig=fig)
  with col2:
    st.write ('Metadata Nodes')

