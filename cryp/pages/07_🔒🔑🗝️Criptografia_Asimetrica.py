import streamlit as st

st.title("Aritmética Modular")

st.write("La aritmética modular es un sistema matemático que trata con números enteros, pero en lugar de trabajar con números continuos, se enfoca en los residuos de la división.")

st.write("**Definición básica:**")

st.write("En la aritmética modular, dos números enteros se consideran equivalentes si tienen el mismo residuo cuando se dividen por un número fijo llamado módulo. Si dos números 'a' y 'b' tienen el mismo residuo cuando se dividen por el módulo 'p', se escriben como 'a ≡ b (mod p)'.")

st.write("**Ejemplo:**")

st.write("Si el módulo es 5, entonces 8 y 3 son equivalentes módulo 5, ya que ambos tienen un residuo de 3 cuando se dividen por 5. Por lo tanto, '8 ≡ 3 (mod 5)'.")

st.write("**Operaciones básicas:**")

st.write("- **Adición:** La suma de dos números módulo 'p' es el residuo de la suma cuando se divide por 'p'.")
st.write("- **Sustracción:** La resta de dos números módulo 'p' es el residuo de la resta cuando se divide por 'p'.")
st.write("- **Multiplicación:** El producto de dos números módulo 'p' es el residuo del producto cuando se divide por 'p'.")
st.write("- **Exponentiación:** El resultado de elevar un número a una potencia módulo 'p' es el residuo de la potencia cuando se divide por 'p'.")

st.write("**Grupos en Aritmética Modular:**")

st.write("En el contexto de la aritmética modular, un grupo es un conjunto de elementos junto con una operación binaria que satisface las propiedades de cierre, asociatividad, identidad e inverso. Los grupos pueden ser aditivos o multiplicativos.")

st.write("**Grupo Aditivo:**")

st.write("El conjunto de números enteros módulo 'p' con la operación de adición forma un grupo abeliano. Este grupo cumple las siguientes propiedades:")
st.write("- **Cierre:** Si 'a' y 'b' están en el conjunto, entonces 'a + b' también está en el conjunto.")
st.write("- **Asociatividad:** La suma es asociativa: '((a + b) + c) ≡ (a + (b + c)) (mod p)'.")
st.write("- **Identidad:** Existe un elemento identidad '0' tal que 'a + 0 ≡ a (mod p)' para todo 'a' en el conjunto.")
st.write("- **Inverso:** Para cada 'a', existe un inverso '-a' tal que 'a + (-a) ≡ 0 (mod p)'.")

st.write("**Grupo Multiplicativo:**")

st.write("El conjunto de números enteros coprimos con 'p' (es decir, aquellos entre 1 y p-1 que no tienen factores comunes con 'p') con la operación de multiplicación forma un grupo multiplicativo. Este grupo cumple las siguientes propiedades:")
st.write("- **Cierre:** Si 'a' y 'b' están en el conjunto, entonces 'a * b' también está en el conjunto.")
st.write("- **Asociatividad:** La multiplicación es asociativa: '((a * b) * c) ≡ (a * (b * c)) (mod p)'.")
st.write("- **Identidad:** Existe un elemento identidad '1' tal que 'a * 1 ≡ a (mod p)' para todo 'a' en el conjunto.")
st.write("- **Inverso:** Para cada 'a', existe un inverso 'a^(-1)' tal que 'a * a^(-1) ≡ 1 (mod p)'. Este inverso existe si y solo si 'a' es coprimo con 'p'.")

st.write("**Reglas de la Aritmética Modular:**")

st.write("Las operaciones básicas de la aritmética modular incluyen:")
st.write("- **Adición:** '(a + b) mod p'.")
st.write("- **Sustracción:** '(a - b) mod p'.")
st.write("- **Multiplicación:** '(a * b) mod p'.")
st.write("- **Exponentiación:** '(a^b) mod p'. Esto se calcula de manera eficiente mediante el algoritmo de exponenciación modular.")





# Título y descripción principal
st.title(":closed_lock_with_key: Intercambio de Claves Diffie-Hellman")

# Descripción del protocolo Diffie-Hellman
st.markdown("""
El intercambio de claves **Diffie-Hellman (D-H)** es un protocolo fundamental que permite a dos partes establecer una clave secreta compartida a través de un canal inseguro, como internet.

### Ejemplo de funcionamiento:

1. **Alice y Bob acuerdan un módulo grande** `p` **y un generador** `g`.
2. **Alice elige un secreto aleatorio** `a` **y calcula** `A = g^a mod p`.
3. **Bob elige un secreto aleatorio** `b` **y calcula** `B = g^b mod p`.
4. **Alice envía** `A` **a Bob y Bob envía** `B` **a Alice**.
5. **Alice calcula** `K = B^a mod p`.
6. **Bob calcula** `K = A^b mod p`.

### Seguridad:

La seguridad del protocolo D-H se basa en la dificultad de calcular el logaritmo discreto.

### Problema del logaritmo discreto:

- **Definición:** Dado un módulo `p`, un generador `g` y un elemento `h` en el grupo cíclico `Z/pZ`, encontrar el entero `x` tal que `g^x = h mod p`.

### Dificultad:

El problema del logaritmo discreto se considera computacionalmente difícil para módulos grandes. No se conoce un algoritmo eficiente para resolverlo en general.
""")