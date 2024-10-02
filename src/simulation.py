import copy
import random
import networkx as nx 
from typing import Dict, Any, List, Set
from src.graph import get_dict_info
from src.f_diffusion import Base_DiffusionFunction


class InformationDiffusion_Simulator:
  def __init__(self, G:nx.Graph ) -> None:
    self.G:nx.Graph = G
    self.info:Dict = get_dict_info (G=G)

  def simulate(self, f_diffusion:Dict[ int,Base_DiffusionFunction ], root:Set[int], STEP:int=10 ) -> Dict[ str,Any ]:
    log:Dict[ str,Any ] = { }

    list_nodes_analized:Set[int] = { i for i in root }
    list_nodes_visited :Set[int] = { i for i in root }
    
    for i in range(STEP):
      
      if len(list_nodes_analized) == len(self.G.nodes()):
        break

      list_tmp:Set[int] = set ()
      
      for v in list_nodes_visited:

        f_v = f_diffusion[v]
        neighbors = self.info['neighbors'][v]
        
        for neighbor in neighbors:
          if f_v.diffusion(j=neighbor):
            #log[i+1]['pairs'].append ((v, neighbor))
            list_tmp.add (neighbor)
      
      list_nodes_analized.update ( copy.deepcopy(list_tmp) )
      list_nodes_visited = copy.deepcopy(list_tmp)

      log[i+1] = { 
        'analized' : copy.deepcopy(set(list_nodes_analized)),
        'visited'  : copy.deepcopy(set(list_nodes_visited)) 
      }

    return log
