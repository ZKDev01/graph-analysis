import streamlit as st 

from scipy.stats import pearsonr

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

metadatas = load_name_metadatas ( )
options = st.multiselect ( 'Select Metadatas', metadatas )

btn_create = st.button ( label='Create Vertex' )
btn_load = st.button ( label='Show Vertex' )

is_new_vertex: bool = False

vertex = None

if btn_create and not ( len ( options ) == 0 ):
  vertex = generate_vertex ( name_metadatas=options, N=N )
  is_new_vertex = True

if btn_load or is_new_vertex: 
  if vertex == None:
    vertex = load_vertex ( )
  
  st.write ( '# Vertexs Like a Dataframe' )
  df = convert_vertex_list_to_dataframe ( vertex=vertex )

  if len ( options ) == 0:
    columns = df.columns
    options = [ m for m in metadatas if m in columns ]

  st.write ( df )

  st.write ( '## Analisis Estadistico de los vertices' )
  
  st.write ( '### Analisis de frecuencia de metadatos' )
  
  frequency_dict = { }
  for opt in options:
    frequency_dict[ opt ] = df[ opt ].explode().value_counts()
  for key, frequency_serie in frequency_dict.items ( ):
    st.write ( frequency_serie )
  # pretty print < frequency-dict >
  
  st.write ( '### Analisis de clustering basado en preferencias' )
  # ...

  st.write ( '### Analisis de correlacion entre peliculas y generos' )
  # correlacion de pearson  
  
