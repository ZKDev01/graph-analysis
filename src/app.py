import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes_1 = [ i for i in range(1, 8) ]

nodes_2 = [ 'A', 'B', 'C', 'D' ]

G.add_nodes_from( nodes_1 )

graph = [ 
  ( 1, 2 ),
  ( 1, 3 ),
  ( 2, 3 ),
  ( 2, 5 ),
  ( 4, 5 ),
  ( 5, 6 ),
  ( 5, 7 ),
  ( 6, 7 )
]

# Añadir aristas
G.add_edges_from(graph)

# Graficar el grafo

pos = nx.random_layout(G)

""" 
fig, ax = plt.subplots(figsize=(3,2))
nx.draw_networkx_nodes(
  G,
  pos = pos,
  ax = ax
)
nx.draw_networkx_edges(
  G,
  pos = pos,
  edgelist = G.edges,
  ax = ax
)
"""

nx.draw(G, with_labels=True, pos=pos)
plt.show()