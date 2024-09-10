import random

from src.graph import ( 
  DynamicGraph
)

def model_ER ( graph: DynamicGraph, p: float ) -> DynamicGraph:
  """ 
  Model: Erdos-Renyi 
  """

  for i in range ( graph.N ):
    for j in range ( i+1, graph.N ):
      if random.random ( ) < p:
        graph.add_edge ( i, j )
  
  return graph

def model_WS ( graph: DynamicGraph ) -> DynamicGraph:
  """
  Model: Watts-Strogatz
  """

  return graph

def model_BA ( graph: DynamicGraph ) -> DynamicGraph:
  """ 
  Model: Barabasi-Albert
  """
  
  return graph


