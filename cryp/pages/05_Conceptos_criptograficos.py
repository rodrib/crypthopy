import streamlit as st
import random


# Título
st.title("Generadores de números aleatorios (RNGs)")

# Información sobre los tipos de RNGs
st.write("Son algoritmos o dispositivos que producen secuencias de números que parecen aleatorios. Pueden ser de dos tipos:")
st.write("- **Verdaderamente aleatorios (TRNGs):** Utilizan fuentes físicas impredecibles para generar números aleatorios, como el ruido térmico o la desintegración radiactiva.")
st.write("- **Pseudoaleatorios (PRNGs):** Utilizan un algoritmo matemático para generar números que parecen aleatorios a partir de un valor inicial (semilla).")

def generar_numeros_aleatorios(semilla, cantidad):
    numeros = []
    # Definir el generador de números pseudoaleatorios
    rng = random.Random(semilla)
    # Generar la secuencia de números pseudoaleatorios
    for _ in range(cantidad):
        numeros.append(rng.random())
    return numeros

def main():
    st.title("Generador de Números Aleatorios")

    # Entrada de la semilla
    semilla = st.text_input("Ingrese la semilla para el generador de números aleatorios:")
    try:
        semilla = int(semilla)
    except ValueError:
        st.error("La semilla debe ser un número entero.")

    # Entrada de la cantidad de números a generar
    cantidad = st.number_input("Ingrese la cantidad de números aleatorios a generar:", min_value=1, step=1)

    # Generar números aleatorios si la semilla es válida
    if isinstance(semilla, int):
        numeros_aleatorios = generar_numeros_aleatorios(semilla, cantidad)
        st.write("Números Aleatorios Generados:")
        st.write(numeros_aleatorios)

if __name__ == "__main__":
    main()