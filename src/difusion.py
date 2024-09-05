from src.utils.graph import DynamicGraph

import random

class InformationDiffusion_Simulator:
  def __init__(self, graph: DynamicGraph) -> None:
    self.graph: DynamicGraph = graph
    self.reported_nodes: set = set ( )

  def simulate_step ( self ) -> None:
    # Simular la propagacion de informacion
    new_reported = set ( )
    for reported_node in self.reported_nodes:
      neighbors = self.graph.adj_list [ reported_node ]
      for neighbor in neighbors:
        # Probabilidad de difusion
        if random.random ( ) < 0.5:
          new_reported.add ( neighbor )
    
    # Actualizar el conjunto de nodos 
    self.reported_nodes.update ( new_reported )

    # Permitir cambios dinamicos del grafo: 10% probabilidad de cambio
    if random.random ( ) < 0.1 : 
      self._dynamic_change ( )

  def _dynamic_change ( self ):
    # Ejemplo de cambio dinamico: agregar un nuevo nodo y conectar
    new_node = self.graph.n
    self.graph.add_node ( )
    self.graph.add_edge ( random.randint( 0, new_node-1), new_node )
