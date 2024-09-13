import networkx as nx
import matplotlib.pyplot as plt

import streamlit as st

from src.words import (
  MOVIE_GENRE_LIST,
  MUSIC_GENRE_LIST,
  NODE_TYPES
)

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

from src.dynamic import (
  Dynamic
)

from src.diffusion_functions import (
  Base_DiffusionFunction,
  Probabilistic_DiffusionFunction,
  Metadata_DiffusionFunction,
  MostPopular_DiffusionFunction
)

from src.simulation import (
  InformationDiffusion_Simulator
)

# region: AUXILIAR

def flattern_dict_pairs ( adj_list: dict[ int, list[int] ] ) -> list[ (int, int) ]:
  result = [ ]
  for key, values in adj_list.items ( ):
    for value in values:
      result.append ( (key, value) )
  return result

def get_nx_graph_from_dynamic_graph ( dynamic: DynamicGraph ) -> nx.Graph:
  graph = nx.Graph ( )
  
  nodes = [ i for i in dynamic.ids ]
  edges = flattern_dict_pairs ( dynamic.adj_list )

  graph.add_nodes_from( nodes )
  graph.add_edges_from( edges )
  
  return graph

# endregion: AUXILIAR

# region: DISPLAY-IN-STREAMLIT

def display_dynamic_graph ( dynamic_graph: DynamicGraph ) -> None:
  nx_graph = get_nx_graph_from_dynamic_graph ( dynamic=dynamic_graph )
  fig, ax = plt.subplots ( figsize=(25,25) )
  pos = nx.circular_layout ( G=nx_graph )

  nx.draw ( nx_graph, with_labels=True, pos=pos, ax=ax )
  st.pyplot ( fig=fig )

# endregion: DISPLAY-IN-STREAMLIT



def deploy ( ) -> None:
  st.title ( 'Proyecto de Análisis de Redes Complejas' )

  n_nodes = st.sidebar.number_input ( 'Select a number of nodes', min_value=0, max_value=100 )
  p_model_ER = st.sidebar.number_input ( 'Select a value for model-ER', min_value=0.0, max_value=1.0 )
  step_simulation = st.sidebar.number_input ( 'Select a number of simulation step', min_value=1, max_value=5 )

  dynamic_graph = None

  with st.form ( 'main-form' ):
    
    if n_nodes > 0 and dynamic_graph == None:
      nodes = generator_nodes ( 
        n=n_nodes,
        node_types=NODE_TYPES,
        preferences={
          'movie':MOVIE_GENRE_LIST,
          'music':MUSIC_GENRE_LIST
        }
      )
      dynamic_graph = DynamicGraph ( nodes=nodes )
      
      model_ER ( graph=dynamic_graph, p=p_model_ER )

      st.form_submit_button ( 'Submit Dynamic Graph' )

  if dynamic_graph != None:
    
    multiplex_graph = MultiplexGraph ( )
    multiplex_graph.add_graph ( 'model-ER', dynamic_graph )

    diffusion_functions = { }
    for i in range ( n_nodes ):
      diffusion_functions[ i ] = Probabilistic_DiffusionFunction ( 
        dynamic_graph.nodes[i], 
        p=0.5
      )
    
    root = 0
    select_layer = 'model-ER'
    f_dynamic = Dynamic ( 'add-node' )
    p_dynamic = 0.5

    simulation = InformationDiffusion_Simulator ( 
      graph=multiplex_graph,
      root=root,
      p=p_dynamic
    )
    result = simulation.simulate (
      layer=select_layer,
      diffusion_functions=diffusion_functions,
      dynamic=f_dynamic,
      step=step_simulation
    )

    temporal: TemporalGraph = result [ 'Temporal Graph' ]
    for i, graph in enumerate( temporal.graphs ):
      st.write ( f'Step Simulation { i }' )
      display_dynamic_graph ( dynamic_graph=graph )


if __name__ == '__main__':
  deploy ( )




