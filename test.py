from src.difusion import (
  InformationDiffusion_Simulator,
  DynamicGraph
)
from src.random_models import ( 
  erdos_renyi_model,
)

import random



def test_1 ( ) -> None:
  n = 100
  root = random.randint ( 0, n-1 )
  step = 100

  graph = DynamicGraph ( n )
  graph = erdos_renyi_model ( graph, p=0.5 )

  simulator = InformationDiffusion_Simulator ( graph, root )

  for _ in range ( step ):
    simulator.simulate_step ( )

  print ( f"\n\nNodos con Informacion: { len( simulator.reported_nodes ) }" )
  print ( f'\nNumero de nodos finales: { graph.n }\n\n' )





def main ( ) -> None:
  test_1 ( )

if __name__ == "__main__":
  main ( )
