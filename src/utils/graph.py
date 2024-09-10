


class Node:
  def __init__(self, id: int, node_type: str, name: str, preferences: dict[ str, list[ str ] ]) -> None:
    self.id = id
    self.node_type = node_type
    self.name = name
    self.preferences = preferences
  
  def get_node_by_id ( self, id: int ) -> 'Node':
    return self if id == self.id else None



class DynamicGraph:

  def __init__(self, nodes: list[ Node ]) -> None:
    self.N = len( nodes )
    self.nodes = nodes

    self.adj_list: dict[ int, list[int] ] = { }
    self.degrees: dict[ int, int ] = { }
    for n in nodes:
      self.adj_list[ n.id ] = [ ]
      self.degrees [ n.id ] = 0


  def find_node_by_id ( self, id: int ) -> Node:
    for node in self.nodes:
      if node.id == id:
        return node
    return None

  # OK
  def add_node ( self, node: Node ):
    self.nodes.append ( node )
    self.N += 1

    self.adj_list[ node.id ] = [ ]
    self.degrees [ node.id ] = 0

  # OK
  def remove_node ( self, id: int ):
    self.N -= 1
    del self.adj_list[ id ]
    del self.degrees [ id ]
    
    for key, value in self.adj_list.items ( ) :
      # node = self.find_node_by_id ( key )
      if id in value:
        value.remove ( id )
        self.degrees [ key ] -= 1
    
  # OK
  def add_edge ( self, id_1: int, id_2: int ):
    if not id_1 == id_2:
    
      self.adj_list[ id_1 ].append ( id_2 )
      self.adj_list[ id_2 ].append ( id_1 )
      self.degrees [ id_1 ] += 1
      self.degrees [ id_2 ] += 1

  # NOT TEST
  def remove_edge ( self, id_1: int, id_2: int ):
    if id_1 in self.adj_list [ id_2 ]:

      self.adj_list [ id_1 ].remove ( id_2 )
      self.adj_list [ id_2 ].remove ( id_1 )
      self.degrees [ id_1 ] -= 1
      self.degrees [ id_2 ] -= 1





class MultiplexGraph:

  def __init__ ( self ) -> None:
    self.graphs = { }
  
  def add_graph ( self, identifier: str, graph: DynamicGraph ) -> None:
    self.graphs [ identifier ] = graph






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


