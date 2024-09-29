import pandas as pd 
import networkx as nx 
from typing import List, Dict, Tuple
from src.graph import get_dict_info 
from src.info2json import load_tokens

def get_metadatas (G:nx.Graph) -> List[str]:
  return [ m for m in G.nodes(data=True)[1].keys() ]

def convert_graph_info_to_dataframe (G:nx.Graph) -> pd.DataFrame:

  dict_metadata = [ value[1] for value in G.nodes(data=True) ]
  metadata_name = get_metadatas (G=G)
  dict_database = { }
  
  for key in metadata_name:
    dict_database[key] = [ value[key] for value in dict_metadata ]
  
  dict_database['degree'] = [ degree for (_, degree) in G.degree() ]

  df = pd.DataFrame (dict_database)
  return df

def info_of_metadata_to_dataframe (df: pd.DataFrame, metadata_name: List) -> pd.DataFrame:
  tokens: Dict[str, List[str]] = { name:value for name,value in load_tokens().items() if name in metadata_name } 
  new_df = pd.DataFrame()
  new_df['name'] = df['name']
  for name,value in tokens.items():
    for item in value:
      new_df[item] = df.apply (lambda row: 1 if item in row[name] else 0, axis=1)
  return new_df


def pagerank(G, alpha=0.85, max_iter=100, tol=1.0e-8):
  n = G.number_of_nodes()
  dangling = set(node for node in G.nodes() if G.degree(node) == 0)
  damping_factor = alpha
  teleportation_probability = (1 - damping_factor) / n
  rank = {node: 1.0 / n for node in G.nodes()}
  dangling_rank = 0.0

  for _ in range(max_iter):
    new_rank = {}
    for node in G.nodes():
      if node in dangling:
        new_rank[node] = teleportation_probability
      else:
        new_rank[node] = (1 - damping_factor) * rank[node] / G.out_degree(node)
    for node in G.nodes():
      if node not in dangling:
        new_rank[node] += damping_factor * sum(rank[neighbor] / G.out_degree(neighbor) 
                          for neighbor in G.neighbors(node))
    rank = new_rank
    
    if abs(dangling_rank - rank[dangling.pop()]) < tol:
      break
    dangling_rank = rank[dangling.pop()]

  return rank
