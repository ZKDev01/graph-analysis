from copy import deepcopy
from typing import Any, List, Dict


class Metadata:
  def __init__( self, name: str, value: List[ Any ] ) -> None:
    self.name : str = name
    self.value: list [ str ] = value

  @staticmethod
  def copy ( obj: 'Metadata' ) -> 'Metadata':
    new_obj = deepcopy ( obj )
    return new_obj



class Vertex:
  def __init__( self, name: str, v_type: str, metadatas: List[ Metadata ] ) -> None:
    self.name = name
    self.type = v_type
    self.metadatas = metadatas
  
  def add_metadata ( self, new_metadata: Metadata ) -> bool:
    for metadata in self.metadatas:
      if new_metadata.name == metadata.name:
        return False
    self.metadatas.append ( new_metadata )
    return True

  def update_metadata ( self, new_metadata: Metadata ) -> bool:
    for metadata in self.metadatas:
      if new_metadata.name == metadata.name:
        metadata = Metadata.copy( new_metadata )
        return True
    return False

  def delete_metadata ( self, metadata_name: str ) -> bool:
    for i, metadata in enumerate ( self.metadatas ):
      if metadata.name == metadata_name:
        del self.metadatas[ i ]
        return True
    return False

  @staticmethod
  def copy ( obj: 'Vertex' ) -> 'Vertex':
    new_obj = deepcopy ( obj )
    return new_obj

  @staticmethod
  def convert_to_dict ( obj: 'Vertex' ) -> Dict:
    obj_like_dict = { }
    obj_like_dict[ 'name' ] = obj.name
    obj_like_dict[ 'type' ] = obj.type

    metadatas = { }
    for m in obj.metadatas:
      metadatas[ m.name ] = m.value
    obj_like_dict[ 'metadatas' ] = metadatas
    
    return obj_like_dict

  @staticmethod
  def convert_from_dict ( obj_like_dict: Dict ) -> 'Vertex':
    v_name = obj_like_dict[ 'name' ]
    v_type = obj_like_dict[ 'type' ]
    
    metadatas = [ ]
    for key, value in obj_like_dict[ 'metadatas' ].items( ):
      metadatas.append ( Metadata ( key, value ) )
    
    obj = Vertex ( name=v_name, v_type=v_type, metadatas=metadatas )
    return obj



class DynamicGraph:
  def __init__ ( self, vertex: List [ Vertex ] ) -> None:
    self.vertex = Dict()
    for i, v in enumerate ( vertex ):
      self.vertex [ i ] = v
    
  

""" 



class DynamicGraph:

  def __init__(self, nodes: list[ Node ]) -> None:
    self.nodes = [ node.copy( ) for node in nodes ]

    self.ids = { node.id for node in self.nodes }
    assert len( self.ids ) == len( self.nodes )

    self.adj_list: dict[ int, list[int] ] = { }
    for n in nodes:
      self.adj_list[ n.id ] = [ ]

  def clone_adj_list ( self, adj_list: dict[ int, list[int] ] ):
    for key, value in adj_list.items ( ):
      self.adj_list[ key ] = [ i for i in value ]

  def N ( self ) -> int:
    return len ( self.nodes )

  def find_node_by_id ( self, id: int ) -> Node:
    for node in self.nodes:
      if node.id == id:
        return node
    return None

  # OK
  def add_node ( self, node: Node ):
    if node.id in self.ids:
      node.id = max( self.ids ) + 1
      self.ids.add( node.id )

    self.nodes.append ( node.copy( ) )

    self.adj_list[ node.id ] = [ ]
    return node.id

  # NOT TEST
  def remove_node ( self, id: int ):
    del self.adj_list[ id ]
    
    for key, value in self.adj_list.items ( ) :
      # node = self.find_node_by_id ( key )
      if id in value:
        value.remove ( id )
    
  # OK
  def add_edge ( self, id_1: int, id_2: int ):
    if not id_1 == id_2:
    
      self.adj_list[ id_1 ].append ( id_2 )
      self.adj_list[ id_2 ].append ( id_1 )

  # OK
  def remove_edge ( self, id_1: int, id_2: int ):
    if id_1 in self.adj_list [ id_2 ]:

      self.adj_list [ id_1 ].remove ( id_2 )
      self.adj_list [ id_2 ].remove ( id_1 )





class MultiplexGraph:

  def __init__ ( self ) -> None:
    self.graphs = { }
  
  def add_graph ( self, key: str, graph: DynamicGraph ) -> None:
    self.graphs [ key ] = graph

  def remove_graph ( self, key: str ) -> None:
    try:
      del self.graphs[ key ]
    except:
      raise Exception ( 'Error al eliminar el grafo del multiplex' )

  def get_specific_graph ( self, key: str ) -> DynamicGraph:
    try:
      return self.graphs[ key ]
    except:
      raise Exception ( 'Error al encontrar el grafo' )



class TemporalGraph: 
  def __init__(self, graph: DynamicGraph ) -> None:
    self.initial_graph = graph
    self.graphs = [ graph ]

  def get_initial_graph ( self ) -> DynamicGraph:
    return self.initial_graph

  def get_specific_temporal_graph ( self, t: int ) -> DynamicGraph:
    return self.graphs [ t ]

  def set_new_initial_graph ( self, graph: DynamicGraph ) -> None:
    self.initial_graph = graph
    self.graphs = [ graph ]

  def add_new_temporal_graph ( self, graph: DynamicGraph ) -> None:
    self.graphs.append ( graph )

  def get_last_temporal_graph ( self ) -> DynamicGraph:
    tmp_last = self.graphs [ len( self.graphs ) - 1 ]
    output = DynamicGraph ( tmp_last.nodes )
    output.clone_adj_list ( tmp_last.adj_list ) 
    return output




"""

