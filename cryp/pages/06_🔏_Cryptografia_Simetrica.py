import streamlit as st

st.title("Criptografía Simétrica")

st.write("Un 'cypher' o 'cipher' es una técnica o algoritmo utilizado para cifrar o codificar información de manera que sea incomprensible para aquellos que no tengan la clave o el conocimiento necesario para descifrarlo.")



st.markdown(r"$c = \text{Encrypt}(p, k) \quad \text{y} \quad p = \text{Decrypt}(c, k)$", unsafe_allow_html=True)

# Subtítulo para el concepto de rondas de encriptación
st.subheader("Rondas de encriptación")

# Explicación sobre rondas de encriptación
st.write("""Las 'rondas de encriptación' son pasos repetitivos que se aplican en un algoritmo de cifrado para aumentar la seguridad del proceso.
          Durante cada ronda, se realizan operaciones de transformación en los datos, como substituciones, permutaciones o combinaciones con la clave de cifrado.
          Estas operaciones se aplican de manera iterativa sobre el texto plano o el texto cifrado, dependiendo del algoritmo, y pueden variar en complejidad y número de repeticiones según el diseño del cifrador. 
         El objetivo de las rondas de encriptación es incrementar la resistencia del cifrado ante métodos criptoanalíticos, haciendo que sea más difícil para un atacante descifrar el mensaje sin conocer la clave correcta.""")




st.subheader("Diagrama de rondas de encriptación")

# URL de la imagen
url_imagen = "https://braincoke.fr/assets/static/block_cipher_encryption.e9b60af.cfed321ab98feb7a6c376bf02267b14b.png"

# Mostrar la imagen en Streamlit
st.image(url_imagen, use_column_width=True)


st.subheader("Modos de Operación en Criptografía Simétrica")

resumen = """
En criptografía simétrica, se utilizan varios modos de operación para cifrar y descifrar datos de manera segura. Tres de los principales modos son:

**Electronic Codebook (ECB):**
Cada bloque de texto plano se cifra de forma independiente utilizando la misma clave. Sin embargo, es vulnerable a patrones repetitivos, lo que puede ser explotado por un atacante.

**Cipher Block Chaining (CBC):**
Introduce retroalimentación, combinando cada bloque de texto plano con el bloque cifrado anterior. Más seguro que ECB, pero no es paralelizable.

**Counter (CTR):**
Convierte un cifrador de bloque en un cifrador de flujo, permitiendo la encriptación paralela. Utiliza valores pseudoaleatorios (nonce) para producir texto cifrado final.

Estos modos ofrecen diferentes niveles de seguridad y eficiencia en la criptografía simétrica.
"""

st.markdown(resumen)

url_imagen1 = "https://upload.wikimedia.org/wikipedia/commons/b/b0/BlockcipherModesofOperation.png"

# Mostrar la imagen en Streamlit
st.image(url_imagen1, use_column_width=True)

st.subheader("AES")

resumen1 = """El Estándar de Cifrado Avanzado (AES) es un algoritmo de cifrado simétrico ampliamente utilizado para proteger datos sensibles.
 AES utiliza claves de 128, 192 o 256 bits para cifrar 
y descifrar información de manera segura y eficiente.
"""

st.markdown(resumen1)


############
import streamlit as st
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import base64
import io

# Configuración del título y descripción
st.title("Cifrado y Descifrado de Archivos")
st.write("Esta aplicación permite cifrar y descifrar archivos utilizando el algoritmo AES en modo CBC.")

# Función para cifrar un archivo
def cipher_file(input_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(input_file.read(), AES.block_size))
    return cipher_text

# Función para descifrar un archivo
def decipher_file(input_file, key):
    cipher = AES.new(key, AES.MODE_CBC)
    plain_text = unpad(cipher.decrypt(input_file.read()), AES.block_size)
    return plain_text

# Interfaz de usuario para cargar archivos
encrypt_file = st.file_uploader("Selecciona un archivo para cifrar", type=["txt", "pdf", "png", "jpg"])
decrypt_file = st.file_uploader("Selecciona un archivo para descifrar", type=["enc"])

if encrypt_file is not None:
    st.write("Archivo seleccionado para cifrar:", encrypt_file.name)
    key = st.text_input("Introduce una clave de cifrado (16, 24 o 32 caracteres)", type="password")
    if st.button("Cifrar"):
        if len(key) in [16, 24, 32]:
            cipher_text = cipher_file(encrypt_file, key.encode())
            st.success("¡El archivo ha sido cifrado exitosamente!")
            # Botón de descarga del archivo cifrado
            b64_cipher_text = base64.b64encode(cipher_text).decode()
            href = f'<a href="data:file/enc;base64,{b64_cipher_text}" download="encrypted_file.enc">Descargar Archivo Cifrado</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.error("La longitud de la clave debe ser de 16, 24 o 32 caracteres.")

if decrypt_file is not None:
    st.write("Archivo seleccionado para descifrar:", decrypt_file.name)
    key = st.text_input("Introduce la clave de cifrado utilizada", type="password")
    if st.button("Descifrar"):
        if len(key) in [16, 24, 32]:
            decrypted_file = decipher_file(decrypt_file, key.encode())
            try:
                decrypted_text = decrypted_file.decode('utf-8')
                st.success("¡El archivo ha sido descifrado exitosamente!")
                # Mostrar el contenido del archivo descifrado
                st.text(decrypted_text)
            except UnicodeDecodeError:
                decrypted_text = decrypted_file.decode('latin1')
                st.success("¡El archivo ha sido descifrado exitosamente!")
                st.text(decrypted_text)
        else:
            st.error("La longitud de la clave debe ser de 16, 24 o 32 caracteres.")
