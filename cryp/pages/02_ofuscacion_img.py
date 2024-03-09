import streamlit as st
from PIL import Image
import numpy as np

def ofuscar_imagen(imagen):
    # Convertir la imagen a un arreglo NumPy
    array_imagen = np.array(imagen)

    # Cambiar los valores de los píxeles (ofuscación simple)
    array_imagen = array_imagen + 50  # Puedes ajustar este valor según tus necesidades

    # Crear una nueva imagen a partir del arreglo NumPy modificado
    nueva_imagen = Image.fromarray(array_imagen)

    return nueva_imagen

def main():
    st.title("Ofuscador de Imágenes")

    # Introducción y explicación
    st.write("Este programa ofusca una imagen cambiando los valores de los píxeles.")

    # Subida de imagen
    imagen_original = st.file_uploader("Seleccione una imagen:", type=["jpg", "jpeg", "png"])

    # Botón para ofuscar la imagen
    if st.button("Ofuscar Imagen") and imagen_original:
        # Cargar la imagen desde el archivo
        imagen_pil = Image.open(imagen_original)

        # Ofuscar la imagen
        imagen_ofuscada = ofuscar_imagen(imagen_pil)

        # Mostrar la imagen original y ofuscada
        st.image([imagen_pil, imagen_ofuscada], caption=["Imagen Original", "Imagen Ofuscada"], width=300)

if __name__ == "__main__":
    main()
