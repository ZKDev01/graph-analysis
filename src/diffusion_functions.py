import random

from src.graph import (
  Node,
  DynamicGraph,
  MultiplexGraph,
  TemporalGraph,
)



class Base_DiffusionFunction:
  def __init__(self, node: Node) -> None:
    self.node = node

  def diffusion ( self, graph: DynamicGraph, neighbor: Node ) -> bool:
    return True

  def __str__(self) -> str:
    output = "Always returns TRUE"
    return output

class Probabilistic_DiffusionFunction ( Base_DiffusionFunction ):
  def __init__(self, node: Node, p: float) -> None:
    self.node = node
    self.p = p

  def diffusion(self, graph: DynamicGraph, neighbor: Node ) -> bool:
    return random.random( ) < self.p 
  
  def __str__(self) -> str:
    output = f"Diffusion with a probability: { self.p }"
    return output

class Metadata_DiffusionFunction ( Base_DiffusionFunction ):
  def __init__(self, node: Node, metadata: str, count: int = 1) -> None:
    self.node = node
    self.metadata = metadata
    self.count = count

  def diffusion(self, graph: DynamicGraph, neighbor: Node) -> bool:
    original_preferences = self.node.preferences[ self.metadata ]
    neighbor_preferences = neighbor.preferences[ self.metadata ]
    result = [ preference for preference in original_preferences if preference in neighbor_preferences ]
    return self.count <= len( result )  

  def __str__(self) -> str:
    output = f'Diffusion if the neighbor has N={self.count} common preferences ( preferences={self.metadata} )'
    return output
  
class MostPopular_DiffusionFunction ( Base_DiffusionFunction ):
  def __init__(self, node: Node, value: int) -> None:
    self.node = node
    self.value = value
  
  def diffusion(self, graph: DynamicGraph, neighbor: Node) -> bool:
    adj_list_of_neighbor = graph.adj_list[ neighbor.id ]
    return self.value <= len ( adj_list_of_neighbor )

  def __str__(self) -> str:
    output = f'Diffusion if the neighbor is popular'
    return output


