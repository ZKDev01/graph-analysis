import random

from typing import Dict, Any, Set, List

from src.graph import (
  Vertex,
  DynamicGraph
)


class Base_DiffusionFunction :

  def __init__ ( self, graph: DynamicGraph, i: int ) -> None:
    self.graph = graph
    self.i = i 
  
  def diffusion ( self, j: int ) -> None:
    return True
  
  # poder transformar una funcion a texto, para luego tomarla de los JSON
  def __repr__(self) -> str:
    pass 



class Probabilistic_DiffusionFunction ( Base_DiffusionFunction ) : 

  def __init__(self, graph: DynamicGraph, i: int, p: float) -> None:
    super().__init__(graph, i)
    self.p = p

  def diffusion(self, j: int) -> None:
    return random.random ( ) < self.p
  
  def __repr__(self) -> str:
    pass



class MostPopular_DiffusionFunction ( Base_DiffusionFunction ) :
  
  pass



class Metadata_DiffusionFunction ( Base_DiffusionFunction ) :
  
  pass



""" 

class Probabilistic_DiffusionFunction ( Base_DiffusionFunction ):
  def __init__(self, v: Vertex, p: float) -> None:
    self.v = v
    self.p = p

  def diffusion ( self, graph: DynamicGraph, neighbor: Vertex ) -> bool:
    return random.random( ) < self.p 
  
  def get_name ( self ) -> str:
    output = f"Diffusion with a probability: { self.p }"
    return output

class MostPopular_DiffusionFunction ( Base_DiffusionFunction ):
  def __init__(self, v: Vertex, value: int) -> None:
    self.v = v
    self.value = value
  
  def diffusion(self, graph: DynamicGraph, neighbor: Vertex) -> bool:
    #adj_list_of_neighbor = graph.adj_list[ neighbor ]
    #return self.value <= len ( adj_list_of_neighbor )
    return

  def get_name ( self ) -> str:
    output = f'Diffusion if the neighbor is popular'
    return output

class Metadata_DiffusionFunction ( Base_DiffusionFunction ):
  def __init__(self, node: Vertex, metadata: str, count: int = 1) -> None:
    self.node = node
    self.metadata = metadata
    self.count = count

  def diffusion(self, graph: DynamicGraph, neighbor: Vertex) -> bool:
    original_preferences = self.node.preferences[ self.metadata ]
    neighbor_preferences = neighbor.preferences[ self.metadata ]
    result = [ preference for preference in original_preferences if preference in neighbor_preferences ]
    return self.count <= len( result )  

  def __str__(self) -> str:
    output = f'Diffusion if the neighbor has N={self.count} common preferences ( preferences={self.metadata} )'
    return output

"""

