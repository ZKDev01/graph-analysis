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


import random
from typing import Any




class InformationDiffusion_Simulator:
  def __init__(self, graph: MultiplexGraph, root: int) -> None:
    self.informed = set[int]
    self.graph = graph

    self.root = root
    self.nodes_for_diffusion: set[int] = { root }

  def simulate ( self, layer: str, diffusion_functions: dict[ int, Base_DiffusionFunction ], dynamic: Dynamic, step: int = 10 ) -> TemporalGraph:
    
    # Tomar el grafo de multiplex con layer = layer
    graph = DynamicGraph ( )   # para tener algo
    temporal = TemporalGraph ( graph=None )

    for _ in range ( step ):
      
      # diffusion 

      for n in self.nodes_for_diffusion:
        
        neighbors = graph.adj_list[ n ]
        
        for neighbor in neighbors:
          f = diffusion_functions[ n ]
          
          if f.diffusion ( graph=graph, neighbor=neighbor ):
            
            self.nodes_for_diffusion.add ( neighbor )
        
        self.informed.add ( n )
        self.nodes_for_diffusion.remove ( n )  

      # dynamic

      graph = dynamic.simulate_dynamics ( graph=graph )

      # add like a temporal step in temporal graph

      temporal.add_new_temporal_graph ( graph=graph )

    return temporal

    ## primero partimos de los nodos => nodes_for_diffusion
    ## luego efectuamos para cada nodes_for_diffusion su funcion de difusion 
    ### si es true add in nodes_for_diffusion el nodo que dio true
    ### luego despues que el nodo paso por todos los nodos vecinos se adiciona a informed  
    ## luego de que esto suceda se efectua dynamic al grafo, esto lo que hara es efectuara cambios al grafo segun el objeto
    ## luego que la informacion se difunda y se hayan hecho cambios al grafo se adiciona al temporal graph
    # return temporalgraph luego de iterar n = step veces
    

""" 


class InformationDiffusion_Simulator:
  def __init__(self, graph: DynamicGraph, root: int) -> None:
    self.graph: DynamicGraph = graph
    self.reported_nodes: set = { root }

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

    # Permitir cambios dinamicos del grafo: 10% probabilidad de cambio
    if random.random ( ) < 0.1 : 
      self._dynamic_change ( )

  def _dynamic_change ( self ):
    # Ejemplo de cambio dinamico: agregar un nuevo nodo y conectar
    new_node = self.graph.n
    self.graph.add_node ( )
    self.graph.add_edge ( random.randint( 0, new_node-1), new_node )



"""