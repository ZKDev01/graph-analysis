import networkx as nx 
from typing import Any, Set, List, Dict

def create_graph ( 
    N: int = 100, 
    metadatas: Dict[ str, List[ str ] ] = { },
    model: str = '', 
    param_model: Dict = { } 
  ) -> nx.Graph:
  
  G = nx.Graph ( )
  
  # Generacion de aristas segun un modelo de grafos aleatorios
  if model == 'barabasi-albert':
    G = nx.barabasi_albert_graph ( n=N, m=param_model['m'] )
  if model == 'watts-strogatz':
    G = nx.watts_strogatz_graph ( n=N, k=param_model['k'], p=param_model['p'] )
  if model == '':
    G.add_nodes_from ( [i for i in range(N)] )
  
  return G 

def set_node_attributes ( G: nx.Graph, name_attribute : str, node_attribute: Dict[ int, Any ] ) -> None:
  
  pass

def set_edge_attributes ( G: nx.Graph, name_attribute : str, edge_attribute: Dict[ int, Any ] ) -> None:
  
  pass
