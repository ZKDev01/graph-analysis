import networkx as nx
import matplotlib.pyplot as plt

import streamlit as st

from src.data_faker import (
  generator_name_list,
  generator_tokens_unique_list,
)

from src.random_models import (
  model_ER,
  model_BA,
  model_WS
)







from src.graph import (
  Node,
  DynamicGraph
)





MOVIE_GENRE_LIST = [
  'action',
  'comedy',
  'drama',
  'horror',
  'fantasy'
]

MUSIC_GENRE_LIST = [
  'jazz',
  'rock',
  'pop',
  'classical',
  'hip-hop'
]

def display_node ( node: Node ) -> None:
  preferences = 'Preference: \n'
  for key, value in node.preferences.items ( ) :
    title = f"- { key.upper( ) } => { value }"
    preferences += title + '\n\n'

  st.markdown ( f"""
  **Info del Nodo:** { node.name }\n
  Type: { node.node_type }\n
  
  {preferences}
  """ )

def display_dynamic_graph ( graph: DynamicGraph ) -> None:
  st.markdown ( f"""
  Nodes: { graph.N }
  """ )
  
  st.write ( '## DISPLAY NODES' )
  for n in graph.nodes:
    display_node ( n )

  st.write ( '## DISPLAY EDGES' )
  st.write ( graph.adj_list )

def generate_nodes ( n: int ) -> list [ Node ]:
  name_list = generator_name_list ( n=n ) 
  nodes = [ ]
  for i, name in enumerate ( name_list ):
    tmp = Node ( 
      id=i,
      node_type='Person',
      name=name,
      preferences={ 
        'music_genre' : generator_tokens_unique_list ( word_list=MUSIC_GENRE_LIST ),
        'movie_genre' : generator_tokens_unique_list ( word_list=MOVIE_GENRE_LIST )
      }
    )
    nodes.append ( tmp )
  return nodes

def node_class ( ) -> None:
  st.markdown ( '# Test: Node Class' )

  st.button ( 'RESET', type='primary' )

  name = st.text_input ( 'Nombre', '' )

  movie_options = st.multiselect (
    'Seleccionar generos de peliculas para el nodo',
    MOVIE_GENRE_LIST,
    []
  )
  music_options = st.multiselect (  
    'Seleccionar generos musicales para el nodo',
    MUSIC_GENRE_LIST,
    []
  )

  if st.button ( 'Create Node' ):
    node = Node ( 
      id = 0, 
      node_type = 'Person',
      name=name,
      preferences = {
        'movie_genre' : movie_options,
        'music_genre' : music_options
      } 
    )

    display_node ( node=node )

def dynamic_graph_class ( ) -> None:
  st.markdown ( '# Test: Dynamic Graph Class' )

  st.button ( 'RESET', type='primary' )

  n = st.number_input ( 'Enter a number', min_value=1, max_value=100 )

  if st.button ( 'Create Graph' ):

    nodes = generate_nodes ( n=n )
    graph = DynamicGraph ( nodes=nodes )

    graph = model_ER ( graph=graph, p=0.5 )

    display_dynamic_graph ( graph=graph )

    # test

    graph.remove_node ( 1 )
    st.write ( 'Status Remove: OK' )

    display_dynamic_graph ( graph=graph )






def test_random_models ( ) -> None:
  st.write ( '# Test: Random-Models' )
  st.button ( 'RESET', type='primary' )

def test_data_faker ( ) -> None:
  st.write ( '# Test: Data-Faker' )
  st.button ( 'RESET', type='primary' )

  option = st.selectbox (  
    'Select one',
    ( 
      'Generator-Name-List',
      'Generator-Tokens-Unique-List'
    )
  )

  if option == 'Generator-Name-List':
    st.write ( f'### {option} function' )
    n1 = st.number_input ( 'Enter a number', min_value=1, max_value=100 )
    if st.button ( f'Execute function: {option}' ):
      result1 = generator_name_list ( n=n1 )
      st.write ( f'Results: { n1 } names' )
      for i, name in enumerate ( result1 ):
        st.write ( f'Name { i+1 } => { name }' )

  if option == 'Generator-Tokens-Unique-List':
    st.write ( f'### {option} function' )
    n2 = st.number_input ( 'Enter a number', min_value=1, max_value=100 )
    if st.button ( f'Execute function: {option} using word-list = MOVIE-GENRE-LIST' ):
      result2 = generator_tokens_unique_list ( word_list=MOVIE_GENRE_LIST, n=n2 )
      st.write ( f'Results: { n2 } tokens' )
      for i, token in enumerate ( result2 ):
        st.write ( f'Token { i+1 } => { token }' )









def test ( ) -> None:
  page_names_to_funcs = {
    'Data-Faker' : test_data_faker,
    'Random-Models' : test_random_models
  }
  
  deploy = st.sidebar.selectbox ( 'Seleccione:', page_names_to_funcs.keys(), disabled=False )
  page_names_to_funcs [ deploy ]()

if __name__ == '__main__':
  test ( )


