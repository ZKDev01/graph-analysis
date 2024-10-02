import random
import networkx as nx
from typing import Dict, Any, Set, List


class Base_DiffusionFunction:

  def __init__(self, G:nx.Graph ) -> None:
    self.G: nx.Graph = G
  def set_config (self, i:int) -> None:
    self.i: int = i
  
  def diffusion(self, j:int ) -> bool:
    return True

  def __repr__(self) -> str:
    return f'Base Diffusion Function'

  def get_dict_for_json(self) -> Dict:
    return {
      'type' : 'base'
    }
  
  def calification (self) -> bool:
    return True

class Probabilistic_DiffusionFunction (Base_DiffusionFunction):
  
  def __init__(self, G:nx.Graph ) -> None:
    super().__init__(G)
  
  def set_config(self, i:int, p:float) -> None:
    self.p = p
    return super().set_config(i)

  def diffusion(self, j: int) -> bool:
    return random.random() < self.p
  
  def __repr__(self) -> str:
    return f'Probabilistic Diffusion Function with p={self.p}'
  
  def get_dict_for_json(self) -> Dict:
    return {
      'type' : 'probabilistic',
      'p' : self.p
    }
  
  def calification(self) -> bool:
    return self.p > 0.5

class Population_DiffusionFunction (Base_DiffusionFunction):
  def __init__(self, G: nx.Graph) -> None:
    super().__init__(G)
  
  def set_config(self, i: int, degree: int, neighbors: Dict[int, List]) -> None:
    self.degree: int = degree
    self.neighbors: Dict[int, List] = neighbors
    return super().set_config(i)
  
  def diffusion(self, j: int) -> bool:
    return len(self.neighbors[j]) >= self.degree

  def __repr__(self) -> str:
    return f'Diffusion depends on the degree of the neighboring node (degree-neighbor >= {self.degree})'

  def get_dict_for_json(self) -> Dict:
    return {
      'type' : 'population',
      'degree' : self.degree
    }
  
  def calification(self) -> bool:
    return self.degree < (len(self.G.nodes())//2)

def interpeter ( key:str, G:nx.Graph, i:int, f_diffusion_params: Dict, info:Dict ) -> Base_DiffusionFunction:
  
  if key == 'base':
    f = Base_DiffusionFunction( G=G )
    f.set_config( i=i )
    return f
  
  if key == 'probabilistic':
    f = Probabilistic_DiffusionFunction( G=G )
    f.set_config ( i=i, p=f_diffusion_params['p'] )
    return f
  
  if key == 'population':
    f = Population_DiffusionFunction( G=G )
    f.set_config (i=i, degree=f_diffusion_params['degree'], neighbors=info['neighbors'] )
    return f
  
  raise Exception(f'Error: TYPE: {key}')
