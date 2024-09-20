import json

from typing import Dict, List, Any, Set

from src.graph import (
  Metadata,
  Vertex
)

# PATH
CONFIG_VERTEX       = 'config/vertex.json'
CONFIG_GRAPH_PARAMS = 'config/graph_params.json'
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



# FALTA
def load_name_metadatas ( ) -> List[ str ] : 
  return [ 'like-movies', 'like-music' ]



def load_tokens ( metadatas: List [ str ], verbose: bool = False ) -> Dict[ str, List[ str ] ]: 
  dict_tokens: Dict[ str, List[ str ] ] = { }

  with open ( TOKENS_METADATAS, 'r' ) as file:
    json_data = json.load ( file )
    for m in metadatas:
      dict_tokens [ m ] = json_data [ m ]
  
  if verbose:
    print ( dict_tokens )

  return dict_tokens


