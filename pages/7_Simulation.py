import networkx as nx
import streamlit as st
from typing import Dict, List, Any, Set
from src.info2json import load_graph, load_f_diffusion
from src.simulation import InformationDiffusion_Simulator
from src.f_diffusion import Base_DiffusionFunction

G:nx.Graph = load_graph()
f_diffusion:Dict[ int,Base_DiffusionFunction ] = load_f_diffusion( G=G )
simulator = InformationDiffusion_Simulator( G=G )
log = simulator.simulate (
  f_diffusion=f_diffusion, 
  root=[0],
  STEP=5 
)

st.write (f'LOG {log}')



# analisis de los resultados de la simulacion 
# log completo de la simulacion 



