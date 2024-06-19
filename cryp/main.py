import streamlit as st
from PIL import Image


#hola
# Título de la aplicación
st.title("Criptografía")

# Ruta de la imagen en la misma carpeta que el archivo main.py
image_path = "cryptography-agus.jpeg"  # Cambia "cryptography-agus.jpeg" por el nombre de tu imagen

# Cargar y mostrar la imagen
try:
    image = Image.open(image_path)
    # Agregar la imagen debajo del título
    st.image(image, caption="Criptografía", use_column_width=True)
except FileNotFoundError:
    st.error("La imagen no se pudo encontrar. Asegúrate de que el archivo de imagen está en la misma carpeta que el archivo main.py.")

# Título y definición de la criptografía
st.header("Introducción")
st.write("La criptografía es el estudio y la práctica de técnicas seguras de comunicación.")
st.write("Involucra la codificación y decodificación de la información para asegurar la confidencialidad, integridad y autenticidad de los datos.\n")
