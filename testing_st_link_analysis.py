
import streamlit as st 
from st_link_analysis import st_link_analysis, NodeStyle, EdgeStyle

st.set_page_config ( layout='wide' )

elements = {
  "nodes" : [
    { "data": { "id": 1, "label": "Person", "name": "Person01" } },
    { "data": { "id": 2, "label": "Person", "name": "Person02" } },
    { "data": { "id": 3, "label": "Person", "name": "Person03" } },
    { "data": { "id": 4, "label": "Person", "name": "Person04" } },
    { "data": { "id": 5, "label": "Person", "name": "Person05" } }
  ],
  "edges" : [
    { "data": { "id": 11, "label": "Link", "source": 1, "target": 2 } },
    { "data": { "id": 12, "label": "Link", "source": 1, "target": 3 } },
    { "data": { "id": 13, "label": "Link", "source": 2, "target": 3 } },
    { "data": { "id": 14, "label": "Link", "source": 2, "target": 4 } },
    { "data": { "id": 15, "label": "Link", "source": 2, "target": 5 } }
  ]
}

node_style = [
  NodeStyle ( "Person", "#FF7F3E", "name", "person" )
]

edge_styles = [
  EdgeStyle ( "Link", "#2A629A", "content", "description" )
]

st.markdown ( "##: Example" )
st_link_analysis ( 
  elements=elements, 
  layout="cose", 
  node_styles=node_style, 
  edge_styles=edge_styles 
)