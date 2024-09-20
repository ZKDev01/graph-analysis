import streamlit as st 
import altair as alt  

st.set_page_config ( 
  page_title='Home',
  layout='wide',
  page_icon='🦮'
)

markdown = """ 
This is a Data Science Project about Graph Analysis

GitHub Repository: <URL>
"""

logo = 'resources/design_01.png'




def main ( ) -> None:
  st.title ( "Main Page" )
  st.sidebar.success ( 'Select a page above.' )

  with st.expander('**About**'):
    st.write ( markdown )
    _, s, _ = st.columns ( (1, 2, 1) )
    with s:
      st.image ( logo )


if __name__ == '__main__':
  main ( )
