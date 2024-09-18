from faker import Faker
from typing import Dict, List, Set

from src.graph import (  
  Metadata,
  Vertex
)

# OK
def generate_name ( N: int = 1, locale: str = 'en_US' ) -> List[ str ]:
  # possible locale: [ 'en_US', 'it_IT', 'ja_JP', 'es_ES', ... ]
  fake = Faker ( locale=locale )
  names: List[ str ] = [ fake.name() for _ in range ( N ) ]
  return names

# OK
def generate_metadata ( tokens: Set [ str ], metadata_name: str, k: int = -1 ) -> Metadata:
  fake = Faker ( )
  
  if k == -1:
    k = fake.random_int ( min=0, max=len( tokens ) )

  if not ( 0 <= k and k <= len ( tokens ) ):
    raise Exception ( 'k > len(tokens) or k = len(tokens) or k is negatived' )
  
  metadata_value = fake.random_elements ( elements=[ token for token in tokens ], length=k, unique=True )
  metadata = Metadata ( name=metadata_name, value=metadata_value )
  return metadata

# OK
def generate_vertex ( dict_tokens: Dict[ str, Set[ str ] ], name: str, v_type: str ) -> Vertex:
  metadatas: List[ Metadata ] = [ ]
  for key, value in dict_tokens.items ( ):
    metadatas.append ( generate_metadata ( tokens=value, metadata_name=key, k=-1 ) )
  
  vertex = Vertex ( name=name, v_type=v_type, metadatas=metadatas )

  return vertex



# OK
def generate_N_vertex_with_unique_name ( N: int, dict_tokens: Dict[ str, Set[ str ] ], v_type: str ) -> List[ Vertex ]:
  vertex: List[ Vertex ] = [ ]
  names = generate_name ( N=N )

  for i in range ( N ):
    vertex.append ( generate_vertex ( dict_tokens=dict_tokens, name=names[i], v_type=v_type ) )
  
  return vertex


