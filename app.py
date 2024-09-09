import networkx as nx
import matplotlib.pyplot as plt

import streamlit as st

def main ( ) -> None:

  st.write ( '# TESTING' )

  G = nx.Graph()

  nodes = [ i for i in range(1, 100) ]
  edges = [ 
    ( 1, 2 ),
    ( 1, 3 ),
    ( 2, 3 ),
    ( 2, 5 ),
    ( 4, 5 ),
    ( 5, 6 ),
    ( 5, 7 ),
    ( 6, 7 )
  ]

  G.add_nodes_from( nodes )
  G.add_edges_from( edges )

  # Graficar el grafo
  fig, ax = plt.subplots ( figsize=(25,25) )
  pos = nx.circular_layout ( G )

  nx.draw(G, with_labels=True, pos=pos, ax=ax)
  # plt.show()
  
  st.pyplot ( fig=fig )

if __name__ == '__main__':
  main ( )





""" 
from diffusion import (
  InformationDiffusion_Simulator,
  DynamicGraph
)
from src.random_models import ( 
  erdos_renyi_model,
)

import random

def test_1 ( ) -> None:
  n = 100
  root = random.randint ( 0, n-1 )
  step = 100

  graph = DynamicGraph ( n )
  graph = erdos_renyi_model ( graph, p=0.5 )

  simulator = InformationDiffusion_Simulator ( graph, root )

  for _ in range ( step ):
    simulator.simulate_step ( )

  print ( f"Nodos con Informacion: { len( simulator.reported_nodes ) }" )
  print ( f'Numero de nodos finales: { graph.n }' )

"""