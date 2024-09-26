import networkx as nx 
from faker import Faker
from typing import Dict, List, Set, Any
from src.f_diffusion import Base_DiffusionFunction

def generate_name ( N: int, locale: str = 'en_US' ) -> Dict[ int, str ]:
  """ 
  
  """
  fake = Faker ( locale=locale )
  names: Dict[ int, str ]= { i : fake.name() for i in range ( N ) }
  return names

def generate_metadata ( N: int, tokens: List[ str ] ) -> Dict[ int, List[ str ] ]:
  """ 
  OK: falta docstring
  """
  fk = Faker( )
  metadatas: Dict[ int, List[ str ] ] = { }
  for i in range ( N ):
    metadatas[ i ] = fk.random_elements ( 
      elements=tokens,  
      length=fk.random_int(min=0, max=len(tokens)),
      unique=True
    )
  return metadatas

def generate_f_diffusion ( G:nx.Graph ) -> Dict[ int,Base_DiffusionFunction ]:
  """
  
  """
  N: int = len(G.nodes)
  f_diffusion: Dict[ int,Base_DiffusionFunction ] = { i:Base_DiffusionFunction( G=G,i=i ) for i in range(N) }
  return f_diffusion
