import streamlit as st 

from src.utils import (
  generate_vertex,
  convert_vertex_list_to_dataframe
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

vertex = None

if btn_create:
  st.write ( 'generando vertices' )
  vertex = generate_vertex ( name_metadatas=load_name_metadatas( ), N=N )
  is_new_vertex = True

if btn_load or is_new_vertex: 
  if vertex == None:
    vertex = load_vertex ( )
  st.write ( 'mostrando vertices' )
  st.write ( convert_vertex_list_to_dataframe ( vertex=vertex ) )

# TODO: Analisis Estadistico del Dataframe
