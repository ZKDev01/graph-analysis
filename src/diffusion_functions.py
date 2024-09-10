from src.graph import (
  Node,
  DynamicGraph,
  MultiplexGraph,
  TemporalGraph,
)

import random
from typing import Any



# BASELINE OK
class Base_DiffusionFunction:
  def __init__(self, node: Node) -> None:
    self.node = node

  def diffusion ( self, graph: DynamicGraph, neighbor: Node ) -> bool:
    return True

  def __str__(self) -> str:
    output = "Always return TRUE"
    return output



# BASELINE OK
class Probabilistic_DiffusionFunction ( Base_DiffusionFunction ):
  def __init__(self, node: Node, p: float) -> None:
    self.node = node
    self.p = p

  def diffusion(self, graph: DynamicGraph, neighbor: Node ) -> bool:
    return self.p < 0.7 
  
  def __str__(self) -> str:
    output = f"Diffusion with Probalistic { self.p }"
    return output



# BASELINE OK
class Metadata_DiffusionFunction ( Base_DiffusionFunction ):
  def __init__(self, node: Node, metadata: str, count: int = 1) -> None:
    self.node = node
    self.metadata = metadata
    self.count = count

  def diffusion(self, graph: DynamicGraph, neighbor: Node) -> bool:
    return super().diffusion(graph, neighbor)


