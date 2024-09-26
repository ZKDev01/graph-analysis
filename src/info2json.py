import json
import networkx as nx
from typing import Dict, List, Any, Set
from src.graph import get_dict_info, convert_dict_to_graph
from src.f_diffusion import Base_DiffusionFunction, interpeter

# PATH
CONFIG_GRAPH        = 'config/graph.json'
CONFIG_F_DIFFUSION  = 'config/diffusion_functions.json'

TOKENS_METADATAS    = 'config/tokens.json'


# LOAD TOKENS
def load_tokens ( verbose: bool = False ) -> Dict[ str, List[ str ] ]:
  """OK: falta docstring

  Args:
      verbose (bool, optional): _description_. Defaults to False.

  Returns:
      Dict[ str, List[ str ] ]: _description_
  """
  output: Dict[ str, List[str] ] = { } 
  
  with open(TOKENS_METADATAS,'r') as file:
    output = json.load(file)

  if verbose:
    print ( output )
  
  return output

# SAVE-LOAD GRAPH
def save_graph ( G: nx.Graph, verbose: bool = False ) -> None:
  dict_json : Dict = get_dict_info(G=G)
  result = json.dumps ( dict_json )
  with open (CONFIG_GRAPH,'w') as file:
    file.write (result)
  
  if verbose:
    print (result)

def load_graph ( verbose: bool = False ) -> nx.Graph:
  result = None
  with open (CONFIG_GRAPH,'r') as file:
    result = json.load (file)
  G = convert_dict_to_graph(result)

  if verbose:
    print (result)
  return G

# SAVE-LOAD DIFFUSION-FUNCTIONS
def save_f_diffusion ( f_diffusion: Dict[ int,Base_DiffusionFunction ], verbose: bool = False ) -> None:
  tmp = { key:value.get_dict_for_json() for key,value in f_diffusion.items() }
  result = json.dumps ( { 'f-diffusion' : tmp } )
  with open (CONFIG_F_DIFFUSION,'w') as file:
    file.write (result)
  
  if verbose:
    print (result)

def load_f_diffusion ( G:nx.Graph, verbose:bool = False ) -> Dict[ int,Base_DiffusionFunction ]:
  result = None
  with open (CONFIG_F_DIFFUSION,'r') as file:
    result = json.load (file)
  
  f_diffusion: Dict[ int,Base_DiffusionFunction ] = { 
    int(key):interpeter(
      key=value['type'],
      G=G,
      i=int(key),
      f_diffusion_params=value) 
    for key,value in result['f-diffusion'].items() }
  
  if verbose:
    print (f_diffusion)

  return f_diffusion

