from typing import List, Dict, Any

from src.load_metadata import (
  Movie,
  Music,
  load_tokens_from_json
)

# region: LOAD CONFIGURATION

def load_dict_tokens_from_metadatas ( ) -> Dict:
  dict_key_paths = { 
    'like-movie': [ 'metadata/movies.json', Movie.f_parse ],
    'like-music': [ 'metadata/music.json', Music.f_parse ]
  }
  dict_tokens = { }

  for key, values in dict_key_paths.items ( ):
    dict_tokens [ key ] = load_tokens_from_json ( 
      path=values[0], 
      f_parse=values[1],
      key_parse=key )

  return dict_tokens

# endregion

# region: DISPLAY

def display_dict_tokens__console ( load_dict: Dict ) -> None:
  
  pass

def display_dict_tokens__streamlit ( ) -> None:
  
  pass

# endregion
