from faker import Faker
from typing import Dict, List, Set


def generate_name ( N: int = 1, locale: str = 'en_US' ) -> List[ str ]:
  """ 
  
  """
  fake = Faker ( locale=locale )
  names: List[ str ] = [ fake.name() for _ in range ( N ) ]
  return names


def generate_metadata ( tokens: Set[ str ], metadata_name: str, k: int = -1 ) -> None:
  """ 
  
  """
  pass


def generate_xd ( ) -> None:
  """
  
  """
  pass
