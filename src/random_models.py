from src.utils.graph import ( 
  DynamicGraph
)

import random

def erdos_renyi_model ( graph: DynamicGraph, p: float ) -> DynamicGraph:
  
  for i in range ( graph.N ):
    for j in range ( i+1, graph.N ):
      if random.random ( ) < p:
        graph.add_edge ( i, j )
  
  return graph





