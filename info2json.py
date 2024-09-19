import json
from typing import Dict, List, Any, Set

from src.graph import (
  Metadata,
  Vertex
)

CONFIG_VERTEX = 'config/vertex.json'
CONFIG_EDGES = 'config/graph_params.json'

# OK
def save_in_vertex_list_in_JSON ( v: List[ Vertex ] ) -> None:
  dict_json = { 'vertex' : [ Vertex.convert_to_dict( element ) for element in v ] }
  result = json.dumps ( dict_json )
  with open ( CONFIG_VERTEX, 'w' ) as file:
    file.write ( result )

# OK
def load_vertex_list_from_JSON ( verbose: bool = False ) -> List[ Vertex ]:
  result = ''

  # read file from json
  with open ( CONFIG_VERTEX, 'r' ) as file:
    result = json.load ( file )
  print ( 'Vertex' )

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
  
  return True



