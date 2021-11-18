
import streamlit as st
import Introduccion as i
import Regla_asociación as r
import Metricas as m
import Clustering as c

st.set_page_config(
    page_title="Inteligencia artificial",
    page_icon="random",
    layout="centered",
    initial_sidebar_state="expanded",
 )

Opcion=st.sidebar.selectbox("Seleccionar el algoritmo",("--","Reglas de asociación","Metricas de distancia",
"Clustering"))
if Opcion == "Reglas de asociación":
    r.show()
elif Opcion == "Metricas de distancia":
    m.show()
elif Opcion == "Clustering":
    c.show()
else:
    i.show()
   
   


