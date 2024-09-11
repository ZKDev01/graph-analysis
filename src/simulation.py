import random
from typing import Any

from src.graph import (
  Node,
  DynamicGraph,
  MultiplexGraph,
  TemporalGraph,
)

from src.diffusion_functions import (
  Base_DiffusionFunction
)

from src.dynamic import (
  Dynamic
)



class InformationDiffusion_Simulator:

  def __init__(self, graph: MultiplexGraph, root: int) -> None:
    self.graph = graph

    self.root = root
    self.informed: list = [ ]
    self.nodes_for_diffusion: set = { root }

  def simulate ( self, layer: str, diffusion_functions: dict[ int, Base_DiffusionFunction ], dynamic: Dynamic, step: int = 10 ) -> TemporalGraph:
    
    graph = self.graph.get_specific_graph ( layer )   
    temporal = TemporalGraph ( graph=graph )

    for _ in range ( step ):  
      # diffusion 
      
      for n in self.nodes_for_diffusion:
        if n in self.informed:
          continue

        neighbors = graph.adj_list[ n ]
        
        for neighbor in neighbors:
          f = diffusion_functions[ n ]
          
          if f.diffusion ( graph=graph, neighbor=neighbor ):
            
            self.nodes_for_diffusion.add ( neighbor )
        
        self.informed.append ( n )  

      # dynamic
      graph = dynamic.simulate_dynamics ( graph=graph )

      # add like a temporal step in temporal graph
      temporal.add_new_temporal_graph ( graph=graph )

    print ( self.informed )
    print ( self.nodes_for_diffusion )
    return temporal    

""" 


class InformationDiffusion_Simulator:

  def simulate_step ( self ) -> None:
    # Simular la propagacion de informacion
    new_reported = set ( )
    for reported_node in self.reported_nodes:
      neighbors = self.graph.adj_list [ reported_node ]
      for neighbor in neighbors:
        # Probabilidad de difusion    
        if random.random ( ) < 0.2 and not neighbor is self.reported_nodes:
          new_reported.add ( neighbor )
          
    # Actualizar el conjunto de nodos 
    self.reported_nodes.update ( new_reported )

"""