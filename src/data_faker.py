from faker import Faker

from src.graph import (
  Node
)



def generator_name_list ( n: int, localization: str = 'en_US' ) -> list[ str ]:
  # possible locales: [ en_US, it_IT, ja_JP, es_ES, ... ]
  fake = Faker ( locale=localization )
  l = [ ]
  for _ in range ( 0, n ):
    l.append ( fake.name( ) )
  return l

def generator_tokens_unique_list ( word_list: set[ str ], n: int = -1 ) -> list [ str ]:
  fake = Faker ( )

  if n == -1:
    n = fake.random_int ( min=0, max=len(word_list)-1 )

  tokens = fake.random_elements ( elements=word_list, length=n, unique=True )
  return tokens

def generator_nodes ( n: int, node_types: list[ str ], preferences: dict[ str, list ] ) -> list [ Node ]:  
  nodes = [ ]
  names = generator_name_list ( n=n )

  for i, name in enumerate ( names ):

    tmp_preferences = { }
    for key, value in preferences.items ( ):
      tmp_preferences [ key ] = generator_tokens_unique_list ( value )

    tmp_node_type = generator_tokens_unique_list ( node_types, n = 1 )[0]

    node = Node (  
      id=i,
      name=name,
      node_type=tmp_node_type,
      preferences=tmp_preferences
    )
    nodes.append ( node )
  
  return nodes