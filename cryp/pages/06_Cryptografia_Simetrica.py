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
