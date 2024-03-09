import streamlit as st


# Título de la aplicación
st.title("Criptografia")

# URL de la nueva imagen
image_url = "https://elcorreoweb.es/binrepository/criptografia-1_20382928_20200310082329.jpg"

# Agregar la imagen debajo del título
st.image(image_url, caption="Criptografia", use_column_width=True)

# Título y definición de la criptografía
st.header("Introducción")
st.write("La criptografía es el estudio y la práctica de técnicas seguras de comunicación.")
st.write("Involucra la codificación y decodificación de la información para asegurar la confidencialidad, integridad y autenticidad de los datos.\n")
