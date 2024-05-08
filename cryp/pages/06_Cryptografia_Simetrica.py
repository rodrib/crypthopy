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


from streamlit.components.v1 import html as html_component

latex_code = r"""
\documentclass[tikz,border=2mm]{standalone}
\begin{document}
\begin{tikzpicture}[scale=1.5]
% Rondas de encriptación
\foreach \x in {0,1,2,3}{
    \draw (\x*1.5,0) rectangle ++(1,1) node[midway] {$R_{\x}$};
}
% Conexiones
\foreach \x in {0,1,2}{
    \draw[->] (\x*1.5+1,0.5) -- (\x*1.5+1.5,0.5);
}
\draw[->] (3*1.5+1,0.5) -- (3*1.5+1.5,0.5) node[right] {Salida};
\draw[dotted] (4.5,0) -- (4.5,1) node[midway, above] {Proceso de cifrado};
\draw[dotted] (0,-0.5) -- (4.5,-0.5) node[midway, below] {Rondas};
\end{tikzpicture}
\end{document}
"""

st.subheader("Diagrama de rondas de encriptación")

# URL de la imagen
url_imagen = "https://braincoke.fr/assets/static/block_cipher_encryption.e9b60af.cfed321ab98feb7a6c376bf02267b14b.png"

# Mostrar la imagen en Streamlit
st.image(url_imagen, use_column_width=True)

