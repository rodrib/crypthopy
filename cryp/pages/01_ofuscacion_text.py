import streamlit as st

def reemplazar_letras(texto):
    reemplazos = {'e': '3', 'a': '4', 'o': '0', 'i': '1', 'u': '_'}
    texto_ofuscado = ''.join(reemplazos.get(char, char) for char in texto)
    return texto_ofuscado

def main():
    st.title("Ofuscador de Texto")

    # Introducción y explicación
    st.write("Este programa reemplaza algunas letras del texto ingresado por números según una regla específica.")

    # Entrada de texto
    texto_original = st.text_area("Ingrese el texto original:")

    # Botón para ofuscar
    if st.button("Ofuscar"):
        texto_ofuscado = reemplazar_letras(texto_original)
        st.write(f"Texto Ofuscado: {texto_ofuscado}")

if __name__ == "__main__":
    main()


