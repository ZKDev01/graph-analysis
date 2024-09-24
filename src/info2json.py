import json

from typing import Dict, List, Any, Set

from src.graph import (
  Metadata,
  Vertex,
  DynamicGraph
)
from src.diffusion_functions import (
  interpeter, 
  Base_DiffusionFunction
)


# PATH
CONFIG_VERTEX       = 'config/vertex.json'
CONFIG_EDGES        = 'config/edges.json'
CONFIG_F_DIFFUSION  = 'config/diffusion_functions.json'
CONFIG_SIMULATION   = 'config/simulation.json'

TOKENS_METADATAS    = 'metadata/tokens.json'



def save_vertex ( v: List[ Vertex ], verbose: bool = False ) -> None:
  
  if not isinstance ( verbose, bool ):
    raise TypeError ( "[verbose] is not bool type" )

  dict_json = { 'vertex' : [ Vertex.convert_to_dict( element ) for element in v ] }
  result = json.dumps ( dict_json )
  with open ( CONFIG_VERTEX, 'w' ) as file:
    file.write ( result )

  if verbose:
    print ( dict_json )



def load_vertex ( verbose: bool = False ) -> List[ Vertex ]:
  
  if not isinstance ( verbose, bool ):
    raise TypeError ( "[verbose] is not bool type" )

  # read file from json
  with open ( CONFIG_VERTEX, 'r' ) as file:
    result = json.load ( file )

  # transform every dict in vertex-object
  list_v : List[ Vertex ] = [ ]
  for d in result [ 'vertex' ] : 
    tmp = { 
      'name' : d[ 'name' ],
      'type' : d[ 'type' ],
      'metadatas' : d[ 'metadatas' ]
    }
    list_v.append ( Vertex.convert_from_dict ( tmp ) )

  if verbose:
    for i, v in enumerate ( list_v ):
      print ( 'VERTEX', i+1 )
      print ( v )
  
  return list_v



def load_name_metadatas ( ) -> List[ str ] : 

  metadatas = [ ]
  with open ( TOKENS_METADATAS, 'r' ) as file:
    json_data: Dict = json.load ( file )
    metadatas = json_data.keys ( )

  return metadatas



def load_tokens ( metadatas: List [ str ], verbose: bool = False ) -> Dict[ str, List[ str ] ]: 
  dict_tokens: Dict[ str, List[ str ] ] = { }

  with open ( TOKENS_METADATAS, 'r' ) as file:
    json_data = json.load ( file )
    for m in metadatas:
      dict_tokens [ m ] = json_data [ m ]
  
  if verbose:
    print ( dict_tokens )

  return dict_tokens



def save_edges ( adj_list: Dict[ int, List[ int ] ], verbose: bool = False ) -> None:
  
  if not isinstance ( verbose, bool ):
    raise TypeError ( "[verbose] is not bool type" )

  tmp = { }
  for key, value in adj_list.items ( ):
    tmp [ key ] = value
  dict_json = { 'edges' : tmp }
  result = json.dumps ( dict_json )
  with open ( CONFIG_EDGES, 'w' ) as file:
    file.write ( result )

  if verbose: 
    print ( dict_json )
  


def load_edges ( verbose: bool = False ) -> Dict [ int, List[int] ]:

  if not isinstance ( verbose, bool ):
    raise TypeError ( "[verbose] is not bool type" )
  
  # read file from json
  with open ( CONFIG_EDGES, 'r' ) as file:
    result = json.load ( file )

  # transform the dict to adj-list
  adj_list : Dict[ int, List[ int ] ] = { }
  for key, value in result [ 'edges' ].items() : 
    adj_list[ int(key) ] = value
    
  if verbose:
    print ( adj_list )

  return adj_list


def save_diffusion_functions ( input: Dict[ int, Base_DiffusionFunction ], verbose: bool = False ) -> None:
  
  tmp = { }
  for key, value in input.items ( ):
    tmp [ key ] = value.get_dict_for_json ( )
  dict_json = { 'dict-diffusion-functions' : tmp }
  
  result = json.dumps ( dict_json )
  with open ( CONFIG_F_DIFFUSION, 'w' ) as file:
    file.write ( result )

  if verbose:
    print ( result )


def load_diffusion_functions ( graph: DynamicGraph,  verbose: bool = False ) -> Dict [ int, Base_DiffusionFunction ]:
  
  with open ( CONFIG_F_DIFFUSION, 'r' ) as file:
    result = json.load ( file )
  
  # transform 
  output: Dict[ int, Base_DiffusionFunction ] = { }
  for key, value in result[ 'dict-diffusion-functions' ].items ( ):
    output[ int(key) ] = interpeter( key=value['type'], graph=graph , i=int(key), params_f_diffusion=value )

  if verbose: 
    print ( result )
    print ( output )
  
  return output