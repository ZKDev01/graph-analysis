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


# region: DISPLAY

def display_node ( node: Node ) -> None:
  preferences = ""
  for key, value in node.preferences.items ( ):
    preferences += f'- { key } : { value } \n  '

  output = f"""
  Identificador: { node.id }
  Name:          { node.name }
  Type:          { node.node_type }
  Preferences    
  { preferences }
  """
  print ( output )

def display_dynamic_graph ( graph: DynamicGraph ) -> None:
  nodes = graph.nodes
  adj_list = graph.adj_list
  
  print ( 'NODES' )
  for i, node in enumerate ( nodes ):
    print ( f'Node { i+1 }' )
    display_node ( node=node )

  print ( 'ADJ LIST' )
  for key, value in adj_list.items ( ):
    print ( f'Adj Nodes of: { key }' )
    print ( f'Nodes: { value }' )

# endregion

# region: TEST 

def test_data_faker ( ) -> None:
  n=5
  nodes = generator_nodes ( n=n, node_types=NODE_TYPES, preferences={
    'movie': MOVIE_GENRE_LIST,
    'music': MUSIC_GENRE_LIST
  } )
  for i, node in enumerate ( nodes ):
    print ( f'Node { i+1 }' )
    display_node ( node=node )

def test_graph__node ( ) -> None:

  id = 0
  name = generator_name_list( 1 )[0]

  movie_options = generator_tokens_unique_list ( word_list=MOVIE_GENRE_LIST )
  music_options = generator_tokens_unique_list ( word_list=MUSIC_GENRE_LIST )
  node_types = generator_tokens_unique_list ( word_list=NODE_TYPES, n=1 )[0]

  node = Node ( 
    id=id,
    node_type=node_types,
    name=name,
    preferences={
      'movie':movie_options,
      'music':music_options
    }
  )

  display_node ( node=node )

def test_graph__dynamic_graph ( ) -> None:
  n = 5
  nodes = generator_nodes ( n=n, node_types=NODE_TYPES, preferences={
    'movie': MOVIE_GENRE_LIST,
    'music': MUSIC_GENRE_LIST
  } )
  dynamic_graph = DynamicGraph ( nodes=nodes )

  # # MODEL ERDOS-RENYI ( and Add-Edge )
  # model_ER ( dynamic_graph, p=0.5 )
  # display_dynamic_graph ( graph=dynamic_graph )

  # # Add-Node
  # new_node = generator_nodes ( n=1, node_types=NODE_TYPES, preferences={
  #   'movie': MOVIE_GENRE_LIST,
  #   'music': MUSIC_GENRE_LIST 
  # } )[0]
  # new_node.id = n 
  # dynamic_graph.add_node ( node=new_node )
  # display_dynamic_graph ( graph=dynamic_graph )
  
  # Add-Edge, Remove
  
  dynamic_graph.add_edge( 0, 1 )
  dynamic_graph.add_edge( 0, 2 )
  dynamic_graph.add_edge( 0, 3 )

  dynamic_graph.add_edge( 1, 2 )
  dynamic_graph.add_edge( 1, 3 )

  # print ( '=== FINISH ADD EDGES ===' )
  # display_dynamic_graph ( dynamic_graph )

  # dynamic_graph.remove_edge( 1, 2 )

  # print ( '=== FINISH REMOVE EDGE ===' )
  # display_dynamic_graph ( dynamic_graph )

  dynamic_graph.remove_node ( 1 )

  # print ( '=== FINISH REMOVE A NODE ===' )
  display_dynamic_graph ( dynamic_graph )

def test_graph__multiplex_graph ( ) -> None:
  nodes = generator_nodes ( n=5, node_types=NODE_TYPES, preferences={
    'music': MUSIC_GENRE_LIST,
    'movie': MOVIE_GENRE_LIST
  } )
  dynamic_graph_1 = DynamicGraph ( nodes=nodes )
  dynamic_graph_2 = DynamicGraph ( nodes=nodes )

  model_ER ( graph=dynamic_graph_1, p=0.3 )
  model_ER ( graph=dynamic_graph_2, p=0.7 )

  multiplex = MultiplexGraph ( )
  multiplex.add_graph ( key='low-p',  graph=dynamic_graph_1 )
  multiplex.add_graph ( key='high-p', graph=dynamic_graph_2 )

  # display_dynamic_graph ( graph=multiplex.get_specific_graph ( 'low-p' ) )

def test_graph__temporal_graph ( ) -> None:
  nodes = generator_nodes ( n=4, node_types=NODE_TYPES, preferences={
    'music': MUSIC_GENRE_LIST,
    'movie': MOVIE_GENRE_LIST
  } )
  dynamic_graph = DynamicGraph ( nodes=nodes )
  temporal_graph = TemporalGraph ( graph=dynamic_graph )

  temporal_0 = temporal_graph.get_specific_temporal_graph( 0 )
  display_dynamic_graph ( temporal_0 )

def test_dynamics ( ) -> None:
  nodes = generator_nodes ( n=4, node_types=NODE_TYPES, preferences={
    'music': MUSIC_GENRE_LIST,
    'movie': MOVIE_GENRE_LIST
  } )
  graph = DynamicGraph ( nodes=nodes )
  model_ER ( graph=graph, p=0.5 )
  dynamics = Dynamic ( 'add-node' )

  display_dynamic_graph ( graph=graph )
  dynamics.simulate_dynamics ( graph=graph, p=0.3 )
  display_dynamic_graph ( graph=graph )

def test_diffusion_functions ( ) -> None:
  nodes = generator_nodes ( n=5, node_types=NODE_TYPES, preferences={
    'music':MUSIC_GENRE_LIST,
    'movie':MOVIE_GENRE_LIST
  } )
  dynamic_graph = DynamicGraph ( nodes=nodes )
  
  # add-edges
  dynamic_graph.add_edge ( 0,1 )
  dynamic_graph.add_edge ( 0,2 )
  dynamic_graph.add_edge ( 0,3 )

  dynamic_graph.add_edge ( 1,3 )
  dynamic_graph.add_edge ( 1,4 )


  # display_dynamic_graph ( dynamic_graph )

  node = dynamic_graph.nodes[0]
  
  base_f_diffusion = Base_DiffusionFunction ( node )
  print ( 'BASE:', base_f_diffusion.diffusion( graph=dynamic_graph, neighbor=dynamic_graph.nodes[1] ) )

  # high p
  hp_f_diffusion = Probabilistic_DiffusionFunction ( node, p=0.9 )
  # low p
  lp_f_diffusion = Probabilistic_DiffusionFunction ( node, p=0.1 )

  print ( 'HIGH:', hp_f_diffusion.diffusion ( graph=dynamic_graph, neighbor=dynamic_graph.nodes[1] ) )
  print ( 'LOW: ', lp_f_diffusion.diffusion ( graph=dynamic_graph, neighbor=dynamic_graph.nodes[1] ) )

  other_nodes = dynamic_graph.nodes[1:]

  metadata_music_f_diffusion = Metadata_DiffusionFunction ( 
    node=node, 
    metadata='music',
  )
  metadata_movie_f_diffusion = Metadata_DiffusionFunction (
    node=node,
    metadata='movie'
  )
  
  display_node ( node )

  for other_node in other_nodes:
    print ( '======================================' )
    display_node ( other_node )
    result_music = metadata_music_f_diffusion.diffusion ( graph=dynamic_graph, neighbor=other_node )
    result_movie = metadata_movie_f_diffusion.diffusion ( graph=dynamic_graph, neighbor=other_node )
    print ( 'Music Diffusion:', result_music )
    print ( 'Movie Diffusion:', result_movie )

  most_popular_f_diffusion = MostPopular_DiffusionFunction ( node=node, value=2 )

  display_dynamic_graph ( graph=dynamic_graph )
  for other in other_nodes:
    result = most_popular_f_diffusion.diffusion ( graph=dynamic_graph, neighbor=other )
    print ( f'Most Popular Result for {other.name}: {result}' )

def test_simulate_final ( ) -> None:
  # generate multiplex
  n = 10
  nodes = generator_nodes ( 
    n=n,
    node_types=NODE_TYPES,
    preferences={
      'music':MUSIC_GENRE_LIST,
      'movie':MOVIE_GENRE_LIST
    }
  )
  dynamic_graph = DynamicGraph ( nodes=nodes )
  model_ER ( dynamic_graph, p=0.7 )
  multiplex_graph = MultiplexGraph ( )
  multiplex_graph.add_graph ( 'model-ER', dynamic_graph )

  # generate diffusion-functions
  diffusion_functions = { }
  for i in range ( n ):
    diffusion_functions[i] = Probabilistic_DiffusionFunction( dynamic_graph.nodes[i], p=0.5 )
  
  # select a root
  root = 0

  # select a layer
  select_layer = 'model-ER'

  # select a step-number
  step = 5

  # create a dynamic 
  f_dynamic = Dynamic ( 'add-node' )
  p_dynamic = 0.5

  # SIMULATE
  simulation = InformationDiffusion_Simulator ( graph=multiplex_graph, root=root, p=p_dynamic )
  result = simulation.simulate ( 
    layer=select_layer,
    diffusion_functions=diffusion_functions,
    dynamic=f_dynamic,
    step=step
  )
  
  temporal: TemporalGraph = result[ 'Temporal Graph' ]
  informed = result[ 'Informed' ]

  for graph in temporal.graphs:
    display_dynamic_graph ( graph=graph )


# endregion


if __name__ == '__main__':
  # test_data_faker ( )
  # test_graph__node ( )
  # test_graph__dynamic_graph ( )
  # test_graph__multiplex_graph ( )
  # test_graph__temporal_graph ( )
  # test_dynamics ( )
  # test_diffusion_functions ( )

  test_simulate_final ( )
  
  print ( 'OK!' )


