import streamlit as st

def cifrado_cesar(texto, desplazamiento):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            index = ord(char) - ascii_offset
            index = (index + desplazamiento) % 26
            texto_cifrado += chr(index + ascii_offset)
        else:
            texto_cifrado += char
    return texto_cifrado

def cifrado_atbash(texto):
    texto_cifrado = ""
    for char in texto:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            index = ord(char) - ascii_offset
            index = 25 - index  # Reemplazar con el opuesto en el alfabeto
            texto_cifrado += chr(index + ascii_offset)
        else:
            texto_cifrado += char
    return texto_cifrado

def cifrado_columna(texto):
    num_columnas = 3
    longitud_texto = len(texto)
    num_filas = (longitud_texto + num_columnas - 1) // num_columnas
    texto += ' ' * (num_filas * num_columnas - longitud_texto)
    columnas_original = [texto[i::num_filas] for i in range(num_filas)]
    columnas_cifradas = ['[' + col + ']' for col in columnas_original]
    texto_cifrado = ''.join(columnas_cifradas)
   
    return texto_cifrado



def main():
    st.title("Criptografía Clásica")

    st.write("La criptografía clásica abarca una serie de técnicas criptográficas que se desarrollaron antes del auge de la computación moderna. Estas técnicas se caracterizan por su simplicidad matemática y su enfoque manual para el cifrado y descifrado.")

    st.write("Tipos de Criptografía Clásica:")

    st.subheader("Cifrado por sustitución:")
    st.write("- **Cifrado de César:** Reemplaza cada letra por otra letra ubicada a una distancia fija en el alfabeto.")
    st.write("- **Cifrado de Atbash:** Sustituye las letras por su opuesto en el alfabeto.")

    st.subheader("Cifrado por transposición:")
    st.write("- **Cifrado de columna:** Reordena las letras del mensaje en columnas y luego las lee por filas.")
    st.write("- **Cifrado de Vigenère:** Utiliza una tabla de sustitución basada en una palabra clave.")

    # Opciones para el usuario
    seleccion = st.selectbox("Seleccione un tipo de cifrado:", ["Cifrado de César", "Cifrado de Atbash","Cifrado de columna","Cifrado de columna2"])

    if seleccion == "Cifrado de César":
        texto_original = st.text_area("Ingrese el texto original:")
        desplazamiento = st.number_input("Ingrese el valor del desplazamiento:", value=3, step=1)
        if st.button("Cifrar"):
            texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
            st.write("Texto cifrado:", texto_cifrado)

    elif seleccion == "Cifrado de Atbash":
        texto_original = st.text_area("Ingrese el texto original:")
        if st.button("Cifrar"):
            texto_cifrado = cifrado_atbash(texto_original)
            st.write("Texto cifrado:", texto_cifrado)

    elif seleccion == "Cifrado de columna":
        texto_original = st.text_area("Ingrese el texto original:")
        if st.button("Cifrar"):
            texto_cifrado = cifrado_columna(texto_original)
            st.write("Texto cifrado:", texto_cifrado)

  


if __name__ == "__main__":
    main()

st.markdown("Matematica")

st.markdown(r"$e_K : M \rightarrow C$")
