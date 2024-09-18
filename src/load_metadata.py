import json
from typing import Dict, List, Set, Any

# region: TOKENS

class Token:
  def __init__(self, key: int, name: str) -> None:
    self.id = key
    self.name = name

  @staticmethod
  def f_parse ( json_data: Any, key: str = '' ) -> List[ 'Token' ] :
    return [ ]

  def __repr__(self) -> str:
    return f"[{self.id}] - '{self.name}'"


class Music ( Token ):
  def __init__(self, key: int, name: str) -> None:  
    super().__init__(key, name)

  @staticmethod
  def f_parse ( json_data: Any, key: str = 'like-music' ) -> List[ 'Music' ] :
    tokens: List[ Music ] = [ ]
    for item in json_data.get ( key, [ ] ):
      token = Music ( item[ 'id' ], item[ 'name' ] )
      tokens.append ( token )
    return tokens


class Movie ( Token ):
  def __init__(self, key: int, name: str) -> None:
    super().__init__(key, name)

  @staticmethod
  def f_parse( json_data: Any, key: str = 'like-movie' ) -> List[ 'Movie' ] :
    tokens: List[ Movie ] = [ ]
    for item in json_data.get ( key, [ ] ):
      token = Movie ( item[ 'id' ], item[ 'name' ] )
      tokens.append ( token )
    return tokens

# endregion

# region: PARSING JSON

def load_tokens_from_json ( path: str, f_parse, key_parse: str ) -> Set[ Token ]:
  tokens: Set [ Token ] = { }
  with open ( path, 'r' ) as file:
    json_data = json.load ( file )
    tokens = f_parse ( json_data )
  return tokens

# endregion

