
class DynamicGraph:
  def __init__(self, n) -> None:
    self.n = n
    self.adj_list = [ [] for _ in range ( n ) ]
    self.degrees = [ 0 ] * n

  def add_node ( self ):
    self.n += 1
    self.adj_list.append ( [] )
    self.degrees.append( 0 )
  
  def remove_node ( self, index ):
    self.n -= 1
    del self.adj_list[ index ]
    del self.degrees[ index ]

    for i, adj_list in enumerate ( self.adj_list ):
      if index in adj_list:
        adj_list.remove ( index )
        self.degrees [ i ] -= 1
        self.degrees [ index ] -= 1
    
  def add_edge ( self, n1, n2 ):
    if not n1 == n2:
      self.adj_list [ n1 ].append ( n2 )
      self.adj_list [ n2 ].append ( n1 )
      self.degrees [ n1 ] += 1
      self.degrees [ n2 ] += 1

  def remove_edge ( self, n1, n2 ):
    if n1 in self.adj_list [ n2 ]:
      self.adj_list[ n1 ].remove ( n2 )
      self.adj_list[ n2 ].remove ( n1 )
      self.degrees [ n1 ] -= 1
      self.degrees [ n2 ] -= 1


