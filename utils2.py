
from utils import load_tokens 
from src.data_faker import generate_N_vertex_with_unique_name

from info2json import save_in_vertex_list_in_JSON, load_vertex_list_from_JSON

def generate_tokens_with_save_in_JSON_and_load_in_JSON ( ) -> None:
  dict_tokens = load_tokens ( ['like-movies', 'like-music'] )
  v = generate_N_vertex_with_unique_name ( N=10, dict_tokens=dict_tokens, v_type='Person' )
  save_in_vertex_list_in_JSON ( v=v )

if __name__ == '__main__': 
  # generate_tokens_with_save_in_JSON_and_load_in_JSON ( )
  load_vertex_list_from_JSON ( )