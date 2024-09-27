import streamlit as st 
from typing import Dict, List, Set, Any
from src.graph import create_graph, get_dict_info
from src.info2json import load_tokens, save_graph, load_graph

st.write ( "# Generación de Grafos" )

# Input Config
col1, col2 = st.columns([1,2])

with col1:
  ## Vertices del grafo
  N = st.number_input (
    label="Introduce la cantidad de vértices que quiere generar para el grafo",
    min_value=1,
    max_value=1000,
    step=1
  )

with col2:
  ## Metadatos de los Vertices
  tokens = load_tokens()
  metadata_options = tokens.keys()
  metadata_select = st.multiselect ( 
    label='Selecciona los metadatos que desea que tengan los vértices del grafo',
    options=metadata_options 
  )  

## Modelo de Generacion Aleatoria de Aristas 
param_model: Dict = { }

with st.form ('barabasi-albert model'):
  param_model[ 'm' ] = st.number_input (
    label='Selecciona el valor m para el modelo barabasi-albert',
    min_value=1
  )
  btn_model_ba = st.form_submit_button(
    label='Generar grafo con el modelo barabasi-albert'
  )
  with st.expander (label='Info'):
    st.write ('El modelo barabasi-albert funciona ...')

with st.form ('watts-strogatz model'):
  param_model[ 'k' ] = st.number_input (
    label='Selecciona el valor k para el modelo watts-strogatz',
    min_value=1 
  )
  param_model[ 'p' ] = st.number_input (
    label='Selecciona el valor p para el modelo watts-strogatz',
    min_value=0.0,
    max_value=1.0
  )
  btn_model_ws = st.form_submit_button(
    label='Generar grafo con el modelo watts-strogatz'
  )
  with st.expander (label='Info'):
    st.write ('El modelo watts-strogatz funciona ...')

# Buttons
btn_load = st.button (
  label="Mostrar Informacion Breve del Grafo"
)

name_model  = 'barabasi-albert' if btn_model_ba else 'watts-strogatz'
param_model = { 'm': param_model['m'] } if btn_model_ba else { 'k' : param_model['k'], 'p' : param_model['p'] }

description = f"""
**Modelo Seleccionado** {name_model}

Los parametros para la generacion del grafo son: 
- N: {N}
- Metadatas: {metadata_select}
- Parametros del Modelo: {param_model}
"""

G = None
if btn_model_ba or btn_model_ws:
  st.write (description)
  G = create_graph(
    N=N,
    metadatas=tokens,
    model=name_model,
    param_model=param_model
  )
  save_graph(G=G)

if btn_load or not (G == None):
  if G == None: G=load_graph()
  info = get_dict_info(G=G)
  st.write (info)
