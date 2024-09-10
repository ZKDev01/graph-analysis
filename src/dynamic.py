
from src.graph import ( 
  Node, 
  DynamicGraph,
  MultiplexGraph,
  TemporalGraph
)


class Dynamic: 
  
  def __init__(self, *args, **kwargs ) -> None:
    self.add_node = True if 'add_node' in kwargs else False
    self.add_edge = True if 'add_edge' in kwargs else False
    self.remove_node = True if 'remove_node' in kwargs else False
    self.remove_edge = True if 'remove_edge' in kwargs else False
    

  def simulate_dynamics ( self, graph: DynamicGraph ) -> DynamicGraph:
    if self.add_node:
      pass
    if self.add_edge:
      pass

    if self.remove_edge:
      pass
    if self.remove_node:
      pass

    # self._modif_metadatas ( ... )

    return graph
  
  def _add_nodes ( self, graph: DynamicGraph, n: int ):
    pass

  def _add_edges ( self, graph: DynamicGraph, n: int ):
    pass

  def _modif_metadatas ( self, graph: DynamicGraph, n: int ): 
    pass
