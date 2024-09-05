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

