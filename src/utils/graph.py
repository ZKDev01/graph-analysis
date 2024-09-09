
class Node:
  def __init__(self, id: int, node_type: str, name: str, preferences: dict[ str, list[ str ] ]) -> None:
    self.id = id
    self.node_type = node_type
    self.name = name
    self.preferences = preferences
  
  def __str__(self) -> str:
    output = f""" 
    ID: { self.id }
    Name: { self.name }
    Type: { self.node_type }
    Preferences: { self.preferences }
    """
    return output
  
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

  def __str__(self) -> str:
    output = f"""
    N: { self.N }
    Adj. List: { self.adj_list }
    Degrees:   { self.degrees }
    """
    return output


  def find_node_by_id ( self, id: int ) -> Node:
    for node in self.nodes:
      if node.id == id:
        return node
    return None


  def add_node ( self, node: Node ):
    self.nodes.append ( node )
    self.N += 1

    self.adj_list[ node.id ] = [ ]
    self.degrees [ node.id ] = 0

  def remove_node ( self, id: int ):
    self.N -= 1
    del self.adj_list[ id ]
    del self.degrees [ id ]
    
    for key, value in self.adj_list.items ( ) :
      # node = self.find_node_by_id ( key )
      if id in value:
        value.remove ( id )
        self.degrees [ id ] -= 1
    
  def add_edge ( self, id_1: int, id_2: int ):
    if not id_1 == id_2:
    
      self.adj_list[ id_1 ].append ( id_2 )
      self.adj_list[ id_2 ].append ( id_1 )
      self.degrees [ id_1 ] += 1
      self.degrees [ id_2 ] += 1

  def remove_edge ( self, id_1: int, id_2: int ):
    if id_1 in self.adj_list [ id_2 ]:

      self.adj_list [ id_1 ].remove ( id_2 )
      self.adj_list [ id_2 ].remove ( id_1 )
      self.degrees [ id_1 ] -= 1
      self.degrees [ id_2 ] -= 1

class MultiplexGraph:
  def __init__(self, graph: DynamicGraph) -> None:
    self.initial_graph = graph
    self.layers = [ graph ]
  
  



def set_nodes_1 ( ) -> list[ Node ]:
  node_1 = Node ( 
    id=0,
    node_type='PERSON',
    name="person 1",
    preferences= { 
      'movies': [ 'movie 1', 'movie 2' ],
      'songs' : [ 'song 1', 'song 2' ]
    } 
  )
  node_2 = Node ( 
    id=1,
    node_type='PERSON',
    name="person 2",
    preferences= { 
      'movies': [ 'movie 2' ],
      'songs' : [ 'song 1' ]
    } 
  )

  return [ node_1, node_2 ]

def test_Node ( ) -> None:
  pass  

def test_DynamicGraph ( ) -> None:
  pass


def test_MultiplexGraph ( ) -> None:
  pass


