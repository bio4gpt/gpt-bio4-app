streamlit_app.py
import streamlit as st
import pandas as pd

# Carga de archivos
precios = pd.read_csv("PRECIOS_BIO4_PRESENTACION_FINAL.csv")
preguntas = pd.read_csv("PREGUNTAS_20_ABRIL_EMBEDDINGS_FINAL.csv")
with open("BIO4_FICHAS_Y_FUNDAMENTOS_COMPLETO_.txt", "r", encoding="utf-8") as f:
    fichas = f.read()

st.set_page_config(page_title="GPT BIO4 Validado", layout="centered")

st.title("Asistente Validador de Productos BIO4")

consulta = st.text_input("Haz tu pregunta sobre un producto BIO4:")

if consulta:
    coincidencias = preguntas[preguntas["Pregunta"].str.contains(consulta, case=False, na=False)]

    if not coincidencias.empty:
        for i, fila in coincidencias.iterrows():
            st.success(f"**Respuesta oficial:** {fila['Respuesta']}")
    else:
        st.warning("⚠️ No hay una respuesta validada para esta consulta. Por favor, revisa la ortografía o verifica el nombre del producto.")
