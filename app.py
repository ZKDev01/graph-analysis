import streamlit as st
import altair as alt

from typing import List, Dict, Any

from src.graph import (
  Metadata,
  Vertex
)
from src.data_faker import (
  generate_N_vertex_with_unique_name
)

from utils import (
  load_tokens
)



def display_vertex_for_test ( vertex: List[ Vertex ] ):
  for i, v in enumerate ( vertex ):
    print ( f'VERTEX { i+1 }' )
    print ( f'Name: {v.name}' )
    for m in v.metadatas:
      print ( f'Metadata -> { m.name } : { m.value }' )
    print ( '' )

def testing_1 ( ) -> None:
  
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












def main ( verbose: bool = True ) -> None:
  dict_tokens = load_tokens ( keys=[ 'like-movies', 'like-music' ] )
  
  st.write ( '# TOKENS' )
  for key, value in dict_tokens.items ( ):
    st.write ( f"KEY: {key}" )
    st.write ( value )
  
  st.write ( '# GENERATE VERTEX' )
  N = 0

  with st.form ( 'Generate Vertex' ):
    N = st.number_input ( 'N', min_value=0, max_value=100 )
    submit_button = st.form_submit_button ( 'Create' )

  if N > 0 and submit_button:
    st.write ( N )
    # Generate 

    vertex = generate_N_vertex_with_unique_name ( N=N, dict_tokens=dict_tokens, v_type='Person' )
    st.write ( vertex )

    # Save Vertex
    

  if verbose:
    print ( 'TOKENS' )
    print ( dict_tokens )

if __name__ == '__main__':
  main ( verbose=False )






# TEST
## 1. Data Faker (GENERADOR DE NODOS)
## 2. Graph - Node
## 3. Graph - Dynamic Graph
## 4. Graph - Multiplex Graph
## 5. Graph - Temporal Graph
## 6. Dynamic
## 7. Difussion Functions
## 8. Simulate Final 

