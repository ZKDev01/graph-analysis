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



from typing import Dict, Any, List, Set

class InformationDiffusion_Simulator: 
  
  def __init__( self, graph: DynamicGraph, root: int ) -> None:
    self.graph = [ graph ]
    self.root = root
  
  def simulate ( self, diffusion_functions: Dict[ int, Base_DiffusionFunction ], step: int = 10 ) -> Dict[ str, Any ] : 
    
    
    pass

"""



class InformationDiffusion_Simulator:

  def __init__(self, graph: MultiplexGraph, root: int, p: float) -> None:
    self.graph = graph

    self.root = root
    self.visited: list[ int ] = [ ]
    self.informed: list[ int ] = [ root ]

    self.p = p

  def simulate ( self, layer: str, diffusion_functions: dict[ int, Base_DiffusionFunction ], dynamic: Dynamic, step: int = 10 ) -> dict[ str, Any ]:
    
    graph = self.graph.get_specific_graph ( layer )   
    temporal = TemporalGraph ( graph=graph )

    # self.visited => Ya difundio la informacion
    # self.informed => Va a difundir la informacion

    for _ in range ( step ):  
      # crear instancias de ultimo grafo temporal (ultimo paso en la simulacion)
      last_temporal = temporal.get_last_temporal_graph ( )

      # crear nuevo conjunto con los nodes for diffusion
      tmp_visited: list = [ ]
      tmp_informed: list = [ ]
      
      # diffusion for each informed
      for n in self.informed:
        tmp_visited.append ( n ) 

        neighbors = last_temporal.adj_list [ n ]
        
        f = diffusion_functions [ n ] if n in diffusion_functions.keys ( ) else Base_DiffusionFunction ( _ )

        for neighbor in neighbors:
          if f.diffusion ( graph=last_temporal, neighbor=neighbor ):
            tmp_informed.append ( neighbor )

      # evitar repeat diffusion
      for v in tmp_visited:
        self.visited.append ( v )
      for i in tmp_informed:
        self.informed.append ( i )
      
      # dynamic 
      dynamic.simulate_dynamics ( graph=last_temporal, p=self.p )

      # ultimo paso para la iteracion 
      temporal.add_new_temporal_graph ( last_temporal )
    
    output = {
      'Temporal Graph' : temporal,
      'Informed' : self.informed
    }

    return output    


"""