import random

from src.graph import ( 
  Node, 
  DynamicGraph,
  MultiplexGraph,
  TemporalGraph
)

from src.data_faker import (
  generator_tokens_unique_list,
  generator_nodes
)

from src.words import (
  MOVIE_GENRE_LIST,
  MUSIC_GENRE_LIST,
  NODE_TYPES
)



class Dynamic: 
  
  def __init__(self, *args ) -> None:
    """
    Possible options: 
    - add-node

    Future:
    - add-edge
    - remove-node
    - remove-edge
    - modif-metadata
    """
    self.keys = args
    
  def simulate_dynamics ( self, graph: DynamicGraph, p: float ) -> DynamicGraph:
    
    if 'add-node' in self.keys and random.random ( ) < p:
      new_node = generator_nodes (
        n=1,
        node_types=NODE_TYPES,
        preferences={
          'music':MUSIC_GENRE_LIST,
          'movie':MOVIE_GENRE_LIST
        }
      )[0]
      id = graph.add_node ( new_node )

      for node in graph.nodes:
        if node.id != id:
          if random.random ( ) < p:
            graph.add_edge ( id, node.id )

    return graph
