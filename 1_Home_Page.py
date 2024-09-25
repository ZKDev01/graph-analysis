import streamlit as st 

st.set_page_config (
  page_title='Home',
  layout='wide',
  page_icon='🦮'
)

markdown = """
Este es un proyecto para la asignatura **Análisis de Redes Complejas**

GitHub Repository: <URL>
"""

def main ( ) -> None:
  st.title ( 'Main Page' )

  with st.expander ( "**About**" ):
    st.write ( markdown )

if __name__ == '__main__':
  main ( )
