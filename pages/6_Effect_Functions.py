import networkx as nx 
import streamlit as st
import matplotlib.pyplot as plt 
from typing import Dict, Any 
from src.info2json import load_graph, get_dict_info
from src.utils import (
  convert_graph_info_to_dataframe,
  info_of_metadata_to_dataframe,
  get_metadatas
)





G:nx.Graph = load_graph ()
info:Dict = get_dict_info (G=G)
N:int = len(G.nodes)


df_info = convert_graph_info_to_dataframe(G=G)
st.write (df_info)

df_metadata = info_of_metadata_to_dataframe (df=df_info, metadata_name=get_metadatas(G=G))
st.write (df_metadata)

