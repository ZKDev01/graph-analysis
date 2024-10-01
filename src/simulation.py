import random
import networkx as nx 
from typing import Dict, Any, List, Set
from src.graph import get_dict_info
from src.f_diffusion import Base_DiffusionFunction


class InformationDiffusion_Simulator:
  def __init__(self, G:nx.Graph ) -> None:
    self.G:nx.Graph = G
    self.info:Dict = get_dict_info (G=G)

  def simulate(self, f_diffusion:Dict[ int,Base_DiffusionFunction ], root:List[int], STEP:int=10 ) -> Dict[ str,Any ]:
    log:Dict[ int,List ] = { }

    list_A:List[int] = [ ]
    list_B:List[int] = root
    
    for i in range(STEP):
      
      if len(list_A) == len(self.G.nodes()):
        break

      list_tmp:List[int] = [ ]

      log[ i+1 ] = [
        f"List A = {list_A}",
        f"List B = {list_B}"
      ]
      
      for v in list_B:

        log[ i+1 ].append ( f'Node {v} difundiendo información' )
        
        f_v = f_diffusion[v]
        neighbors = self.info['neighbors'][v]
        log[ i+1 ].append ( f'Vecinos de {v} = {neighbors}' ) 
        for neighbor in neighbors:
          if f_v.diffusion(j=neighbor):
            log [ i+1 ].append ( f'Vecino {neighbor} con información' )
            list_tmp.append (neighbor)
      
      list_A.extend ([i for i in list_B if i not in list_A])
      list_B:List[int] = [i for i in list_tmp if i not in list_A]

    log:Dict = {
      'log':log,
      'A' : list_A,
      'B' : list_B 
    } 

    return log
