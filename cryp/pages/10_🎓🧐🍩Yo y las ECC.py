import streamlit as st

# Título en Streamlit
st.title("Yo y las ECC")

resumen = """
Mi historia con respecto a las curvas elipticas viene a traves del Teorema de Fermat, el cual conoci
a la edad de 11  años con la Historia de Andrew Wiles, aunque entendi lo basico quede tambien bastante curioso
con las curvas elipticas, las cuales recien volvi a su estudio ahora que empeze con la criptografia
"""


st.write(resumen)

# Enlace a un documento relacionado
link = "https://web.archive.org/web/20170811071550id_/http://scienzamedia.uniroma2.it/~eal/Wiles-Fermat.pdf"
st.markdown(f"Enlace al documento relacionado: [{link}]({link})")

# Título y enlace al video
video_title = "Universo matemático - 04 - Fermat: el margen más famoso de la historia"
video_link = "https://www.youtube.com/watch?v=S7Qw4vsJMPg"
st.markdown(f"**{video_title}**: [Ver video]({video_link})")


