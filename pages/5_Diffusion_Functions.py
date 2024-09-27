import networkx as nx
import streamlit as st 
from typing import Dict, List, Set, Any
from src.info2json import load_graph, save_f_diffusion, load_f_diffusion 
from src.generators import generate_f_diffusion

G:nx.Graph = load_graph()
f_diffusion = generate_f_diffusion(G=G)

st.write (f_diffusion)

st.write ( '#### SAVE f-Diffusion' )
save_f_diffusion (f_diffusion=f_diffusion)

st.write ( '#### LOAD f-Diffusion' )
f_diffusion_2 = load_f_diffusion (G=G)

st.write ( '### TESTING' )
st.write ( '#### 1' )
st.write ( f_diffusion )

st.write ( '#### 2' )
st.write ( f_diffusion_2 )
