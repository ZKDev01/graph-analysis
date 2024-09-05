from src.difusion import (
  InformationDiffusion_Simulator,
  DynamicGraph
)
from src.random_models import ( 
  erdos_renyi_model,
)



def test_1 ( ) -> None:
  
  # los nodos no estan conectados con aristas aun
  graph = DynamicGraph ( 5 )
  graph = erdos_renyi_model ( graph, p=0.5 )

  simulator = InformationDiffusion_Simulator ( graph )

  for _ in range ( 10 ):
    simulator.simulate_step ( )

  print ( f"\n\nNodos con Informacion: { len( simulator.reported_nodes ) }\n\n" )





def main ( ) -> None:
  test_1 ( )

if __name__ == "__main__":
  main ( )
