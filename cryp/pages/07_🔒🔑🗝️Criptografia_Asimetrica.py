import streamlit as st

st.title(":🧮 : Aritmética Modular")

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

st.markdown("""
    ### Compromiso

En 1976, Whitfield Diffie y Martin Hellman publicaron un método para establecer un secreto compartido entre dos partes, permitiendo un canal de comunicación eficiente. Este método genera una llave privada conocida por ambas partes para encriptar y desencriptar información simétricamente. Aunque la criptografía asimétrica es ineficiente para compartir muchos mensajes extensos, es ideal para compartir una llave de encriptación simétrica.

El protocolo Diffie-Hellman establece un canal de comunicación asimétrica para compartir información en una única ocasión por sesión. Las partes generan una llave simétrica a partir de sus claves privadas y públicas, permitiendo un canal de comunicación simétrico descifrable solo por ellos con una llave compartida.
""")

st.markdown("""
    ### Protocolo
""")

import base64
# Nota antes de la animación
st.markdown("**Nota:** En la animación que sigue, cada parte tiene un espacio privado (seguro para los secretos) y comparten un espacio público disponible para ellos y cualquier tercero.")

# URL de la animación GIF
animation_url = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-1.gif"

# Mostrar la animación desde la URL
st.markdown(f'<img src="{animation_url}" alt="Animación del intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


# Segunda parte de la descripción
st.markdown("""
            
En lugar de Alice y Bob definir una llave pública y una llave privada respectivamente, solo nos interesa que definan su llave privada (`a` y `b`) y que acuerden entre sí, expuestos al público, dos valores `g` y `p`.
""")

# URL de la segunda animación GIF
animation_url_2 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-2.gif"

# Mostrar la segunda animación desde la URL
st.markdown(f'<img src="{animation_url_2}" alt="Animación del intercambio de claves Diffie-Hellman, segunda parte">', unsafe_allow_html=True)

# Tercera parte de la descripción
st.markdown("""
Note que al pie de cada región llevamos un registro de las variables a las que han tenido acceso sus respectivos usuarios.
""")

# URL de la tercera animación GIF
animation_url_3 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-3.gif"

# Mostrar la tercera animación desde la URL
st.markdown(f'<img src="{animation_url_3}" alt="Registro de variables en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


# Cuarta parte de la descripción
st.markdown("""
Con sus respectivas claves privadas, Alice y Bob computan un valor combinado con el generador `g` (recuerde que `g` es público). Este proceso de ‘mezclar’ los valores tiene un sentido matemático específico que impide que se pueda deshacer la operación (No es imposible pero sí en exceso difícil y costoso). Respectivamente, Alice y Bob produjeron los valores `ag` y `bg` de los cuales no se pueden inferir las claves privadas `a` y `b`. Sin `p`, esta operación es imposible.
""")

# URL de la cuarta animación GIF
animation_url_4 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-4.gif"

# Mostrar la cuarta animación desde la URL
st.markdown(f'<img src="{animation_url_4}" alt="Proceso de mezclar valores en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


# Quinta parte de la descripción
st.markdown("""
Una vez generados estos cifrados, Alice y Bob los intercambian. Note que como aún no hay un canal seguro de comunicación, `ag` y `bg` son públicos.
""")

# URL de la quinta animación GIF
animation_url_5 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-5.gif"

# Mostrar la quinta animación desde la URL
st.markdown(f'<img src="{animation_url_5}" alt="Intercambio de cifrados en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)

# Sexta parte de la descripción
st.markdown("""
Nuevamente realizamos la operación de ‘mezclado’. Alice mezclará el cifrado público que acaba de recibir de Bob con su clave privada (`bg` con `a`, produce `abg`). Bob, hará lo mismo con su clave privada y el cifrado público que recibió de Alice (`ag` con `b`, produce `abg`).
""")

# URL de la sexta animación GIF
animation_url_6 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-6.gif"

# Mostrar la sexta animación desde la URL
st.markdown(f'<img src="{animation_url_6}" alt="Operación de mezclado en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


# Séptima parte de la descripción
st.markdown("""
Note que ahora Alice y Bob comparten un cifrado irreversible (idéntico para ambos) el cual pueden utilizar para encriptar cualquier mensaje consecuente. Alice y Bob pueden ahora establecer un canal de comunicación seguro, con encriptación simétrica.

Veamos ahora, que únicamente Alice y Bob pueden generar la llave simétrica `abg`. El público tiene acceso al generador `g`, el valor `p` y las llaves cifradas `ag` y `bg`. No hay forma de ‘mezclar’ estos valores de forma tal que generen `abg`. Intentar ‘mezclar’ `bg` con `ag` produciría algo como `abgg`, lo cual es un valor completamente distinto y que no sirve para descifrar los mensajes entre Alice y Bob. ¡Hemos establecido un canal seguro de encriptación simétrica!
""")

# URL de la séptima animación GIF
animation_url_7 = "https://mantimantilla.github.io/Theory-of-Computation-Encryption/_images/Animacion-7.gif"

# Mostrar la séptima animación desde la URL
st.markdown(f'<img src="{animation_url_7}" alt="Establecimiento de canal seguro en el intercambio de claves Diffie-Hellman">', unsafe_allow_html=True)


import streamlit as st

st.markdown("""
Vulnerabilidades
---

El procedimiento parece robusto, pero su intención es solo escudar a 2 partidos de un ojo fisgón. ¿Qué pasa cuando introducimos a una tercera parte, Mallory, que tiene el poder de interceptar y manipular mensajes entre partes en la red? Tenemos también la preocupación de que información secreta de alguna de las partes sea liberada al público. ¿Podemos satisfacer que los mensajes previos están seguros?

Ataque de intermediario (Man in the Middle)
---

Suponga un mismo escenario donde Alice y Bob quieren establecer un canal de comunicación de encriptación simétrica, solo que ahora una tercera parte, Mallory, puede intervenir sobre la información que viaja en la red. Por ejemplo, si Alice quisiera mandar su propuesta de un generador `g` a Bob, Mallory sabría que esto está sucediendo evitar que esto suceda, o escoger su propio mensaje para enviarle a Bob. Note que hasta ahora, nuestro método de comunicación no tiene forma de validar el origen de un mensaje en la red, por lo que Mallory puede estar seguro de que su intromisión en el canal de Alice y Bob no es detectable (aún).

El concepto de este ataque es bastante sencillo. Todo lo que debe hacer Mallory para poder interpretar todos los futuros mensaje entre Alice y Bob es suplantarlos al momento de generar la llave compartida, de forma que Mallory comparte una llave con Bob y una con Alice.

1. Alice y Bob acuerdan un `g` y `p` públicos y generan sus llaves privadas respectivas.
2. Alice genera `ag` y lo publica en la red con la intención de que lo reciba Bob. Bob hace lo mismo para Alice con `bg`.
3. Mallory intercepta estos mensajes y evita que lleguen al destinatario correspondiente.
4. Mallory genera su propia llave privada `m` y produce `mg`.
5. Mallory responde a Alice con `mg` suplantando a Bob. Alice cree que lo que acaba de recibir es `bg`.
6. Mallory responde a Bob con `mg` suplantando a Alice. Bob cree que lo que acaba de recibir es `ag`.
7. Alice y Bob calculan respectivamente `mag` y `mbg`.
8. Mallory calcula `mag` y `mbg`. Ahora comparte un secreto con el cual establecer un canal encriptado simétrico con ambos Alice y Bob. Estos no se han percatado del ataque.

Cualquier cifrado enviado por Alice con la intención de que lo reciba únicamente Bob, llega primero a Mallory. Mallory puede decidir hacer lo que quiera con este. Si la intención es solo mediar la comunicación entre Alice y Bob, Mallory debe descifrar el cifrado entrante y encriptarlo con el secreto contrario. Esto le permite editarlo, borrarlo, o incluso compartirlo con otros.

Esta vulnerabilidad fue descubierta pronto, por lo cual se volvió una práctica común agregar un paso de autenticación al cifrado simétrico. Entran ahora en juego las llaves públicas.

Forward secrecy (PFS)
---

Forward secrecy es la intención de proteger mensajes pasados en caso de que su cifrado haya sido guardado por terceros y el secreto compartido sea publicado. En este caso, la responsabilidad sobre la liberación de estos mensajes no recae sobre alguna falla de Diffie-Hellman. En un inicio mencionamos la noción de una sesión de comunicación. La idea de tener sesiones cortas sobre las cuales habilitar el canal de comunicación es beneficiosa ya que cada vez que se inicie una sesión, la llave compartida puede generarse desde cero en cada ocasión, de forma que, si se libera la clave, solo los mensajes de esa sesión son vulnerables. En teoría, nada impide que utilicemos una nueva llave para cada mensaje o para cada sub-cadena de 126 bits o menos. Recordemos que comunicarse por encriptación asimétrica es un proceso costoso, por lo que quisiéramos minimizar su uso. Cada vez que intercambiamos claves y generamos un secreto compartido estamos efectuando encriptación asimétrica, ya depende de los dueños del canal establecer la frecuencia con la que se generan estas llaves efímeras.
""")

