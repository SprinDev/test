import streamlit as st
api_key = st.secrets["api_key"]
from groq import groq



st.set_page_config(page_title="Desafio 6", page_icon=":guardsman:", layout="wide")
st.title("Desafio 6: Análise de Dados com Pandas")

nombre = st.text_input("Ingresa tu nombre:")
if nombre:
    st.write(f"Hola, {nombre}! Bienvenido al Desafio 6.")

if st.button("Hola!"):
    st.write(f"Hola, {nombre}! Espero que estés disfrutando del desafío.")