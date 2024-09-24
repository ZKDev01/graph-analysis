import random
from typing import Dict, Any, List, Set

from src.graph import (
  Metadata,
  Vertex,
  DynamicGraph
)

from src.diffusion_functions import (
  Base_DiffusionFunction
)


class InformationDiffusion_Simulator: 
  
  def __init__( self, graph: DynamicGraph, root: int ) -> None:
    self.graph = [ graph ]
    self.initial = graph
    self.root = root
  
  def simulate ( self, diffusion_functions: Dict[ int, Base_DiffusionFunction ], step: int = 10, clean_historial: bool = True ) -> Dict[ str, Any ] : 
    
    if clean_historial: self.graph = [ self.initial ]

    log: Dict[ int, Dict ] = { }
    visited = [ self.root ]
    ok = [ ]

    for i in range ( step ):
      
      current_graph = self.graph [ i ]
      tmp_visited = [ ]
      tmp_ok = [ ]

      for v in visited:
        tmp_ok.append ( v )
        neighbors_v = current_graph.adj_list[v]

        f = diffusion_functions[ v ] if v in diffusion_functions.keys ( ) else Base_DiffusionFunction ( current_graph, i=v )

        for n in neighbors_v:
          if f.diffusion ( j=n ):
            tmp_visited.append ( n )
      
      ok.extend ( tmp_ok )
      visited = [ i for i in tmp_visited if i not in ok ]

      log[ i ] = { 
        'vertices visitados' : visited
      }

      self.graph.append ( DynamicGraph.copy(current_graph) )
    
    return log


      # crear instancias del ultimo grafo temporal (ultimo paso en la simulacion)
      # crear nuevo conjunto con los nodos for diffusion : tmp-visited y tmp-informed
      # diffusion for each informed  FOR in INFORMED
      ## tmp-visited append ( informed[i] )
      ## neighbor of informed[i]
      ## for neighbor in neighbors of informed [i]
      ## f = d_f[n] if n in diffusion_functions.keys ( ) else Base_DiffusionFunction ( _ )



    pass
