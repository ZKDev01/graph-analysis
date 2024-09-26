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
    log:Dict[ str,Any ] = { }

    list_A:List[int] = [ ]
    list_B:List[int] = root
    
    for i in range(STEP):
      
      list_tmp:List[int] = [ ]

      for v in list_B:
        f_v = f_diffusion[v]
        neighbors = self.info['neighbors'][v]
        for neighbor in neighbors:
          if f_v.diffusion(j=neighbor):
            list_tmp.append (neighbor)
      
      list_A.extend ([i for i in list_B if i not in list_A])
      list_B:List[int] = [i for i in list_tmp if i not in list_A]
    
    return log
