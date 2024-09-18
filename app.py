# import streamlit as st
# import altair as alt

from typing import List, Dict, Any

from src.graph import (
  Metadata,
  Vertex
)
from src.data_faker import (
  generate_N_vertex_with_unique_name
)


def display_vertex_for_test ( vertex: List[ Vertex ] ):
  for i, v in enumerate ( vertex ):
    print ( f'VERTEX { i+1 }' )
    print ( f'Name: {v.name}' )
    for m in v.metadatas:
      print ( f'Metadata -> { m.name } : { m.value }' )
    print ( '' )


def main ( ) -> None:
  # st.image ( image='resources/design_01.png', caption='presentación' )
  
  dict_tokens = {
    'Like-Music': { 'pop', 'rock', 'hip-hop', 'rap' },
    'Like-Movie': { 'action', 'fantasy', 'horror', 'comedy' }
  }

  vertex = generate_N_vertex_with_unique_name ( N=10, dict_tokens=dict_tokens, v_type='Person' )
  target = vertex[ 0 ]
  display_vertex_for_test ( [target] )
  
  print ( 'OBJECT TO DICT' )
  
  obj_like_dict = Vertex.convert_to_dict( target )
  print ( obj_like_dict )
  
  print ( 'DICT TO OBJECT' )

  obj = Vertex.convert_from_dict ( obj_like_dict=obj_like_dict )
  display_vertex_for_test ( [obj] )

if __name__ == '__main__':
  main ( )






# TEST
## 1. Data Faker
## 2. Graph - Node
## 3. Graph - Dynamic Graph
## 4. Graph - Multiplex Graph
## 5. Graph - Temporal Graph
## 6. Dynamic
## 7. Difussion Functions
## 8. Simulate Final 

