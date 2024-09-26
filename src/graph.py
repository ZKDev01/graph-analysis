import networkx as nx 
from typing import Any, Set, List, Dict
from src.generators import generate_metadata, generate_name

def create_graph ( 
    N: int = 100, 
    metadatas: Dict[ str, List[ str ] ] = { },
    model: str = '', 
    param_model: Dict = { } 
  ) -> nx.Graph:
  # TODO: Falta algunas opciones para la generacion de grafos aleatorios especificos

  G = nx.Graph ( )
  
  # Generacion de aristas segun un modelo de grafos aleatorios
  if model == 'barabasi-albert':
    G = nx.barabasi_albert_graph ( n=N, m=param_model['m'] )
  if model == 'watts-strogatz':
    G = nx.watts_strogatz_graph ( n=N, k=param_model['k'], p=param_model['p'] )
  if model == '':
    G.add_nodes_from ( [i for i in range(N)] )
  
  # set-name-for-vertex
  set_node_attributes ( G=G, name_attribute='name', node_attribute=generate_name(N=N) )
  # set-metadatas-for-vertex
  for name_attribute, values in metadatas.items ( ):
    metadatas = generate_metadata( N=N, tokens=values )
    set_node_attributes ( G=G, name_attribute=name_attribute, node_attribute=metadatas )

  return G 

def convert_dict_to_graph ( info: Dict ) -> nx.Graph:
  """OK: falta docstring

  Args:
      info (Dict): _description_

  Returns:
      nx.Graph: _description_
  """
  # this dict has nodes, edges, nodes-metadata, edges-metadata in keys()
  nodes_metadata = info['nodes-metadata']
  edges_metadata = info['edges-metadata']
  G = nx.Graph()
  G.add_nodes_from (nodes_metadata)
  G.add_edges_from (edges_metadata)
  return G

def get_dict_info ( G: nx.Graph ) -> Dict :
  """OK: falta docstring

  Args:
      G (nx.Graph): _description_

  Returns:
      Dict: _description_
  """
  info:Dict = { 
    'nodes' : [i for i in G.nodes],
    'edges' : [e for e in G.edges],
    'nodes-metadata' : [i for i in G.nodes(data=True)],
    'edges-metadata' : [e for e in G.edges(data=True)]
  }
  info['neighbors'] = { i:[j for j in G[i]] for i in info['nodes'] }
  return info

def set_node_attributes ( 
    G: nx.Graph, 
    name_attribute : str, 
    node_attribute: Dict[ int, List[ str ] ] 
  ) -> None:
  """OK: falta docstring

  Args:
      G (nx.Graph): _description_
      name_attribute (str): _description_
      node_attribute (Dict[ int, List[ str ] ]): _description_
  """
  nx.set_node_attributes ( G=G, name=name_attribute, values=node_attribute )

def set_edge_attributes ( 
    G: nx.Graph, 
    name_attribute : str, 
    edge_attribute: Dict[ int, Any ] 
  ) -> None:
  """OK: falta docstring

  Args:
      G (nx.Graph): _description_
      name_attribute (str): _description_
      edge_attribute (Dict[ int, Any ]): _description_
  """
  nx.set_edge_attributes ( G=G, name=name_attribute, values=edge_attribute )
