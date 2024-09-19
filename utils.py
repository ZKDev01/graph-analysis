import json
from typing import List, Dict, Any, Set

TOKENS_PATH = 'metadata/tokens.json'

# region: LOAD CONFIGURATION

# falta
def load_keys_from_tokens ( ) -> List[ str ]:
  return [ 'like-movies', 'like-music' ]

def load_tokens ( keys: List[ str ] ) -> Dict[ str, List[ str ] ]:
  dict_tokens: Dict[ str, List[ str ] ] = { }
  
  with open ( TOKENS_PATH, 'r' ) as file:
    json_data = json.load ( file )
    for key in keys:
      dict_tokens[key] = json_data[key]

  return dict_tokens

# endregion

# region: DISPLAY

def display_dict_tokens__console ( load_dict: Dict ) -> None:
  
  pass

def display_dict_tokens__streamlit ( ) -> None:
  
  pass

# endregion
