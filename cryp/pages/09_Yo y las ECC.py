import streamlit as st

# Título en Streamlit
st.title("Yo y las ECC")

# Enlace a un documento relacionado
link = "https://web.archive.org/web/20170811071550id_/http://scienzamedia.uniroma2.it/~eal/Wiles-Fermat.pdf"
st.markdown(f"Enlace al documento relacionado: [{link}]({link})")
