import random

from src.graph import ( 
  DynamicGraph
)

def model_ER ( graph: DynamicGraph, p: float ) -> DynamicGraph:
  """ 
  Model: Erdos-Renyi 
  - p = 1 $->$ grafo completo
  - p = 0 $->$ grafo sin aristas

  El modelo de Erdos-Renyi es un grafo aleatorio con $N$ vértices y 
  $M$ aristas que se asignan con probabilidad $p$ de manera independiente. 
  Cualquier topología generada en la red es igual de probable.
  """
  N = graph.get_number_of_vertexs ( )
  for i in range ( N ):
    for j in range ( i+1, N ):
      if random.random ( ) < p:
        graph.add_edge ( i, j )
  
  return graph



def model_WS ( graph: DynamicGraph, avg_degree: int, rewiring_prob: float ) -> DynamicGraph:
  """
  Model: Watts-Strogatz

  El modelo parte de un grafo con $N$ nodos donde estos nodos se conectan a sus dos vecinos más cercanos describiendo una forma de anillo. 
  Esta red en forma de anillo tiene un coeficiente de clustering alto, pero también el diámetro del grafo lo es. 
  """
  return graph



def model_BA ( graph: DynamicGraph ) -> DynamicGraph:
  """ 
  Model: Barabasi-Albert

  El modelo Barabasi-Albert genera las aristas a partir del grado de los nodos. 
  A mayor grado del nodo mas probable es que genere una nueva arista en ese nodo. 
  Este sistema se conoce como conexión preferencial (preferential attachments) y 
  se puede explicar con la paradoja de "the rich get richer"
  """
  return graph


