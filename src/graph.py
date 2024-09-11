




class Node:
  def __init__(self, id: int, node_type: str, name: str, preferences: dict[ str, list[ str ] ]) -> None:
    self.id = id
    self.node_type = node_type
    self.name = name
    self.preferences = preferences
  
  def get_node_by_id ( self, id: int ) -> 'Node':
    return self if id == self.id else None

  def copy ( self ) -> 'Node':
    return Node ( 
      id=self.id,
      node_type=self.node_type,
      name=self.name,
      preferences=self.preferences 
    )




class DynamicGraph:

  def __init__(self, nodes: list[ Node ]) -> None:
    self.ids = { node.id for node in nodes }
    assert len( self.ids ) == len( nodes )

    self.nodes = [ node.copy( ) for node in nodes ]

    self.adj_list: dict[ int, list[int] ] = { }
    for n in nodes:
      self.adj_list[ n.id ] = [ ]

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




