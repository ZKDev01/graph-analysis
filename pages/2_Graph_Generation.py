import streamlit as st 
from typing import Dict, List, Set, Any

st.write ( "Generación de Vértices" )

# Input Config

## Vertices del grafo
N = st.number_input (
  label="Introduce la cantidad de vértices que quiere generar para el grafo",
  min_value=1,
  max_value=1000,
  step=1
)

## Metadatos de los Vertices
metadata_options = [ 'movie-like', 'music-like' ]
metadata_select = st.multiselect ( 
  label='Selecciona los metadatos que desea que tengan los vértices del grafo',
  options=metadata_options 
)

## Modelo de Generacion Aleatoria de Aristas 
model_options = [ 'barabasi-albert', 'watts-strogatz', 'empty-graph' ]
model_select = st.selectbox (
  label='Selecciona el modelo de generacion de aristas para el grafo',
  options=model_options
) 

param_model: Dict = { }
## If model is 'barabasi-albert'
if model_options == 'barabasi-albert':
  param_model[ 'm' ] = st.number_input (
    label='Selecciona el valor m para el modelo barabasi-albert',
    min_value=1
  )
## if model is 'watts-strogatz
if model_options == 'watts-strogatz':
  param_model[ 'k' ] = st.number_input (
    label='Selecciona el valor k para el modelo watts-strogatz',
    min_value=1 
  )
  param_model[ 'p' ] = st.number_input (
    label='Selecciona el valor p para el modelo watts-strogatz',
    min_value=0.0,
    max_value=1.0
  )

# Buttons

btn_create = st.button (  
  label="Crear Grafo"
)
btn_load = st.button (
  label="Mostrar Informacion Breve del Grafo"
)

if btn_create:
  st.write ( param_model )
  st.write ( model_select )

if btn_load:
  pass

