import pandas as pd 
import networkx as nx 
import streamlit as st 
import matplotlib.pyplot as plt 
from typing import Dict, List
from sklearn.cluster import KMeans
from src.graph import get_dict_info
from src.info2json import load_graph

# load graph
G:nx.Graph = load_graph ()
info:Dict = get_dict_info (G=G)

node_features = { node:G.degree(node) for node in G.nodes() }
df = pd.DataFrame (
  node_features.items(), 
  columns=['Node','Degree']
)

# Clustering
K = len(G.nodes)

result = [ ]
for i in range(1, K+1):
  kmeans = KMeans (n_clusters=i, max_iter=300)
  kmeans.fit (df)
  result.append (kmeans.inertia_)

st.write (result)

K_SELECT = 2
clustering = KMeans (n_clusters=K_SELECT, max_iter=300)
clustering.fit (df)
df['Clusters'] = clustering.labels_
st.write (df)
# Las agrupaciones que se formaron es tomando degree un grupo las de mayor degree y otro grupo las de menor degree
# esta tomando como caracteristica, podria decirse como: nodos populares y nodos no populares 

# Centralidad

# dataframe de degree

