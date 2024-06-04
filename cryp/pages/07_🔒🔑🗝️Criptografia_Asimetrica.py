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


import streamlit as st

st.title("Intercambio de Llaves y el Problema del Logaritmo Discreto")

st.subheader("Intercambio de Llaves")

st.write("""
El intercambio de llaves es un proceso fundamental en la criptografía que permite a dos partes (por ejemplo, Alice y Bob) establecer una llave compartida sobre un canal inseguro. Una de las técnicas más conocidas para el intercambio de llaves es el protocolo de Diffie-Hellman.
""")

st.write("""
En el protocolo de Diffie-Hellman, ambos participantes acuerdan públicamente dos números: una base \( g \) y un módulo \( p \). Cada participante elige un número secreto privado (\( a \) para Alice y \( b \) para Bob) y calcula un valor público a partir de estos (\( g^a \mod p \) para Alice y \( g^b \mod p \) para Bob). Luego, intercambian estos valores públicos y, utilizando su propio número privado, cada uno puede calcular la llave compartida:
""")

st.write("""
Para Alice:
\[ \text{Clave compartida} = (g^b \mod p)^a \mod p \]

Para Bob:
\[ \text{Clave compartida} = (g^a \mod p)^b \mod p \]

Debido a la propiedad matemática de las exponenciaciones modulares, ambas partes obtienen la misma llave compartida.
""")

st.subheader("Problema del Logaritmo Discreto")

st.write("""
El problema del logaritmo discreto es un problema matemático difícil que constituye la base de la seguridad del protocolo de Diffie-Hellman y de muchos otros sistemas criptográficos. En términos simples, el problema es el siguiente:

Dado un número \( y \) que es el resultado de \( g^x \mod p \), encontrar el exponente \( x \) es computacionalmente difícil.

Formalmente, si se conoce \( y = g^x \mod p \), determinar \( x \) es el problema del logaritmo discreto. La dificultad de este problema asegura que, incluso si un atacante intercepta los valores públicos intercambiados, no pueda fácilmente determinar la llave compartida.
""")

st.write("""
El problema del logaritmo discreto es considerado difícil porque, para números grandes, no existe un algoritmo eficiente que pueda resolverlo en un tiempo razonable. Esto proporciona la base para la seguridad de varios sistemas criptográficos.
""")

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