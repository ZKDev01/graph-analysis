import json
from src.graph import Vertex, Metadata

def main ( ) -> None:
  n1 = Vertex ( 
    name='Person1', 
    v_type='Person', 
    metadatas= [ 
      Metadata ( name='like-movie', value=[ 'action', 'comedy' ] ),
      Metadata ( name='like-music', value=[ 'hip-hop', 'pop' ] ) 
    ] )
  n2 = Vertex ( 
    name='Person2', 
    v_type='Person', 
    metadatas= [ 
      Metadata ( name='like-movie', value=[ 'horror', 'comedy' ] ),
      Metadata ( name='like-music', value=[ 'rock', 'pop' ] ) 
    ] )
  v = { 
    'vertex' : [ Vertex.convert_to_dict( n1 ), Vertex.convert_to_dict( n2 ) ]
  }

  result = json.dumps( v )
  with open ( 'config/vertex.json', 'w' ) as file:
    file.write ( result )

if __name__ == '__main__':
  main ( )
