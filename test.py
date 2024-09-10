import networkx as nx
import matplotlib.pyplot as plt

import streamlit as st

from src.utils.graph import (
  Node,
  DynamicGraph
)

from src.utils.data_faker import (
  generator_name_list,
  generator_tokens_unique_list,
)

from src.random_models import (
  erdos_renyi_model
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

    graph = erdos_renyi_model ( graph=graph, p=0.5 )

    display_dynamic_graph ( graph=graph )

    # test

    graph.remove_node ( 1 )
    st.write ( 'Status Remove: OK' )

    display_dynamic_graph ( graph=graph )







def test ( ) -> None:
  page_names_to_funcs = {
    'Node Class': node_class,
    'Dynamic Graph Class': dynamic_graph_class
  }
  
  deploy = st.sidebar.selectbox ( 'Seleccione:', page_names_to_funcs.keys(), disabled=False )
  page_names_to_funcs [ deploy ]()

if __name__ == '__main__':
  test ( )


