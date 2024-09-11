import networkx as nx
import matplotlib.pyplot as plt

import streamlit as st

from src.data_faker import (
  generator_name_list,
  generator_tokens_unique_list,
  generator_nodes
)

from src.random_models import (
  model_ER,
  model_BA,
  model_WS
)

from src.graph import (
  Node, 
  DynamicGraph,
  MultiplexGraph,
  TemporalGraph
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
  **Name:** { node.name }\n
  Type: { node.node_type }\n
  
  {preferences}
  """ )

def display_dynamic_graph ( graph: DynamicGraph ) -> None:
  st.write ( '## DISPLAY NODES' )
  for n in graph.nodes:
    display_node ( n )

  st.write ( '## DISPLAY EDGES' )
  st.write ( graph.adj_list )







def test_data_faker ( ) -> None:
  st.write ( '# Test: Data-Faker' )
  st.button ( 'RESET', type='primary' )

  option = st.selectbox (  
    'Select one',
    ( 
      'Generator-Name-List',
      'Generator-Tokens-Unique-List',
      'Generator-Nodes'
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

  if option == 'Generator-Nodes':
    st.write ( f'### {option} function' )
    n3 = st.number_input ( 'Enter a number', min_value=1, max_value=100 )
    if st.button ( f'Execute function: {option}' ):
      preferences = { 
        'movie' : MOVIE_GENRE_LIST,
        'music' : MUSIC_GENRE_LIST
      }
      result3 = generator_nodes ( n=n3, node_types=[ 'Teacher', 'Chef', 'Artist', 'Programmer' ], preferences=preferences )
      st.write ( f'Results: { n3 } nodes' )
      for i, node in enumerate ( result3 ):
        st.write ( f'#### Node { i+1 }' )
        display_node ( node=node )

def test_graph__node ( ) -> None:
  st.write ( '# Test: Graph - Node Class' )
  st.button ( 'RESET', type='primary' )

  id = st.number_input ( 'Identifier', min_value=0, max_value=100 )
  name = st.text_input ( 'Name' )

  movie_options = st.multiselect (
    'Select movie genres for the node',
    MOVIE_GENRE_LIST,
    []
  )
  music_options = st.multiselect (  
    'Select music genres for the node',
    MUSIC_GENRE_LIST,
    []
  )

  if st.button ( 'Create Node' ):
    node = Node ( 
      id = id,
      node_type = 'Programmer',
      name=name,
      preferences= { 
        'movie' : movie_options,
        'music' : music_options
      }
    )
    display_node ( node=node )

def test_graph__dynamic_graph ( ) -> None:
  st.write ( '# Test: Graph - Dynamic Graph Class' )
  st.button ( 'RESET', type='primary' )

  dynamic_graph = None

  n = st.number_input ( 'Enter a number', min_value=0, max_value=100 )
  preferences = { 
    'movie' : MOVIE_GENRE_LIST,
    'music' : MUSIC_GENRE_LIST
  }
  node_types = [ 'Teacher', 'Chef', 'Artist', 'Programmer' ]
  
  if n > 0:
    nodes = generator_nodes ( n=n, node_types=node_types, preferences=preferences )
    dynamic_graph = DynamicGraph ( nodes=nodes )
  
  if dynamic_graph:
    option = st.selectbox (
      'Select one', [
        'Display Dynamic Graph',
        'Add-Node',
        'Remove-Node',
        'Add-Edge',
        'Remove-Edge'
      ]
    )

def test_graph__multiplex_graph ( ) -> None:
  st.write ( '# Test: Graph - Multiplex Graph Class' )
  st.button ( 'RESET', type='primary' )

def test_graph__temporal_graph ( ) -> None:
  st.write ( '# Test: Graph - Temporal Graph Class' )
  st.button ( 'RESET', type='primary' )

def test_random_models ( ) -> None:
  st.write ( '# Test: Random-Models' )
  st.button ( 'RESET', type='primary' )





def test ( ) -> None:
  page_names_to_funcs = {
    'Data Faker' : test_data_faker,
    'Graph - Node' : test_graph__node,
    'Graph - Dynamic Graph' : test_graph__dynamic_graph,
    'Graph - Multiplex Graph' : test_graph__multiplex_graph,
    'Graph - Temporal Graph' : test_graph__temporal_graph
  }
  
  deploy = st.sidebar.selectbox ( 'Seleccione:', page_names_to_funcs.keys(), disabled=False )
  page_names_to_funcs [ deploy ]()

if __name__ == '__main__':
  test ( )


