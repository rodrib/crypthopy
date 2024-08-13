import streamlit as st
from cryptography.fernet import Fernet
from PyPDF2 import PdfReader

# Funciones
def generarKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def encryp(file, key):
    fernet = Fernet(key)
    file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    return file_data, encrypted_data

def mostrar_contenido_pdf(file):
    pdf_reader = PdfReader(file)
    texto_pdf = ""
    for page in pdf_reader.pages:
        texto_pdf += page.extract_text()
    return texto_pdf

# Generar y mostrar la clave
st.title("Cifrador de Archivos PDF")


key = generarKey()
st.write("Clave generada:")
st.code(key.decode(), language="text")

uploaded_file = st.file_uploader("Cargar un archivo PDF", type="pdf")

