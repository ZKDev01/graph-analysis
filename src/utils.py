from pandas import DataFrame
from typing import Dict, List, Set, Any

from src.graph import (
  Vertex,
  Metadata,
  DynamicGraph
)
from src.data_faker import (
  generate_N_vertex_with_unique_name
)
from src.info2json import (
  save_vertex, 
  load_vertex,
  load_tokens,
  load_name_metadatas
)


def generate_vertex ( name_metadatas: List[ str ], N: int = 100 ) -> List[ Vertex ]:
  dict_tokens = load_tokens ( name_metadatas )
  v = generate_N_vertex_with_unique_name ( N=N, dict_tokens=dict_tokens, v_type='Person' )
  save_vertex ( v=v )
  return v



def convert_vertex_list_to_dataframe ( vertex: List[ Vertex ] ) -> DataFrame:
  data = [ ]
  for v in vertex:
    row = {'Name': v.name, 'Type': v.type}
    metadatas_dict = {}
    for meta in v.metadatas:
      metadatas_dict[meta.name] = meta.value
    row.update(metadatas_dict)
    data.append(row)

  df = DataFrame ( data )
  return df