import streamlit as st

# Título en Streamlit
st.title("Yo y las ECC")

# Enlace a un documento relacionado
link = "https://web.archive.org/web/20170811071550id_/http://scienzamedia.uniroma2.it/~eal/Wiles-Fermat.pdf"
st.markdown(f"Enlace al documento relacionado: [{link}]({link})")

# Título y enlace al video
video_title = "Universo matemático - 04 - Fermat: el margen más famoso de la historia"
video_link = "https://www.youtube.com/watch?v=S7Qw4vsJMPg"
st.markdown(f"**{video_title}**: [Ver video]({video_link})")