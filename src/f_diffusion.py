import random
import networkx as nx
from typing import Dict, Any, Set, List


class Base_DiffusionFunction:

  def __init__(self, G:nx.Graph, i:int ) -> None:
    self.G: nx.Graph = G
    self.i: int = i  

  def diffusion(self, j:int ) -> bool:
    return True

  def __repr__(self) -> str:
    return f'Base Diffusion Function'

  def get_dict_for_json(self) -> Dict:
    return {
      'type' : 'base'
    }

class Probabilistic_DiffusionFunction (Base_DiffusionFunction):
  
  def __init__(self, G:nx.Graph, i:int, p:float) -> None:
    super().__init__(G, i)
    self.p = p
  
  def diffusion(self, j: int) -> bool:
    return random.random() < self.p
  
  def __repr__(self) -> str:
    return f'Probabilistic Diffusion Function'
  
  def get_dict_for_json(self) -> Dict:
    return {
      'type' : 'probabilistic',
      'p' : self.p
    }





def interpeter ( key:str, G:nx.Graph, i:int, f_diffusion_params: Dict ) -> Base_DiffusionFunction:
  if key == 'base':
    f = Base_DiffusionFunction( G=G, i=i )
    return f
  if key == 'probabilistic':
    f = Probabilistic_DiffusionFunction( G=G, i=i, 
      p=f_diffusion_params['p'] )
    return f
  raise Exception('Error')
