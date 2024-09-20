import streamlit as st 

from src.utils import (
  generate_vertex
)

from src.info2json import (
  load_vertex,
  load_name_metadatas
)

st.title ( "Generación de Vértices" )

N = st.number_input ( 
  label='Introduce la cantidad de vértices que quiere generar para el grafo:',
  min_value=1,
  max_value=200,
  step=1 )

btn_create = st.button ( label='Create vertex' )
btn_load = st.button ( label='Show vertex' )

is_new_vertex: bool = False

tokens = None

if btn_create:
  st.write ( 'generando vertices' )
  tokens = generate_vertex ( name_metadatas=load_name_metadatas( ), N=N )
  is_new_vertex = True

if btn_load or is_new_vertex: 
  if tokens == None:
    tokens = load_vertex ( )
  st.write ( 'mostrando vertices' )
  st.write ( tokens )

