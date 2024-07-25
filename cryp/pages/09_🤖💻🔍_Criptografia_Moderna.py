import streamlit as st

# Título de la aplicación
st.title("Infraestructura de Llave Pública (PKI)")

# Descripción de la PKI
st.write("""
La Infraestructura de Llave Pública (PKI) es un criptosistema que define roles, políticas y procedimientos para distribuir y revocar certificados firmados utilizando criptografía asimétrica. Se utiliza ampliamente para asegurar la comunicación segura a través de internet y otros sistemas.

### Componentes de la PKI:

- **Autoridad Certificadora (CA)**: Entidad que emite y gestiona certificados digitales.
- **Autoridad Registradora (RA)**: Facilita la verificación de identidad de los solicitantes de certificados antes de enviar la solicitud a la CA.
- **Autoridad Validadora (VA)**: Encargada de verificar la autenticidad de un certificado digital.
- **Sellos de Tiempo**: Servicios que proporcionan evidencia de que los datos existían en un momento específico.
- **Repositorios con Información Adicional**: Almacenan y distribuyen certificados y listas de revocación.

### TLS (Transport Layer Security):

TLS es un protocolo criptográfico que asegura las comunicaciones en internet mediante el uso de PKI. Establece un canal seguro para el intercambio de datos mediante autenticación, integridad de datos y confidencialidad.

### PKCS (Public Key Cryptography Standards):

PKCS es un conjunto de estándares para criptografía asimétrica, principalmente alrededor del algoritmo RSA. Define formatos de clave pública, operaciones criptográficas y gestión de certificados digitales. Es ampliamente utilizado en organizaciones para asegurar la autenticación y la comunicación segura.
""")

# Links
st.markdown("- [TLS en Wikipedia](https://es.wikipedia.org/wiki/Transport_Layer_Security)")
st.markdown("- [PKCS en Wikipedia](https://es.wikipedia.org/wiki/Public_Key_Cryptography_Standards)")

import streamlit as st

# Título de la sección
st.title("Sistemas de Pruebas Interactivos (SPI)")

# Descripción de los SPI
st.markdown("""
En el ámbito de la criptografía, los sistemas de pruebas interactivos (SPI) desempeñan un papel crucial en la verificación de información sin revelar secretos. Estos sistemas permiten a un probador (que posee información confidencial) demostrar a un verificador (que no posee dicha información) que cumple con ciertas condiciones sin revelar la información en sí.

### Principio fundamental de los SPI:

Los SPI se basan en el concepto de conocimiento cero, donde el probador puede demostrar al verificador que posee cierta información sin revelarla durante el proceso.

### Funcionamiento de los SPI:

1. El probador y el verificador acuerdan un protocolo de comunicación.
2. El probador envía un mensaje inicial al verificador, que puede incluir información pública y/o compromisos criptográficos.
3. El verificador desafía al probador con una serie de preguntas o tareas según el protocolo.
4. El probador responde a los desafíos utilizando cálculos criptográficos y/o revelaciones parciales de información.
5. El verificador verifica las respuestas y decide si aceptar o rechazar la prueba.

### Propiedades clave de los SPI:

- **Seguridad**: El verificador no obtiene información confidencial incluso si la prueba falla.
- **Completitud**: Si el probador posee realmente la información, podrá convencer al verificador con alta probabilidad.
- **Solidez**: Si el verificador acepta la prueba, significa que el probador realmente posee la información requerida.

### Aplicaciones de los SPI en criptografía:

- **Firmas digitales**: Verificar la posesión de una clave privada sin revelarla.
- **Autenticación de identidad**: Demostrar la identidad sin exponer contraseñas.
- **Criptografía de curva elíptica**: Intercambio seguro de claves entre dos partes.
- **Pruebas de conocimiento cero**: Construcción de pruebas que demuestran la posesión de información sin divulgarla.

### Ejemplos de SPI en criptografía:

- Protocolo Fiat-Shamir
- Protocolo Guillou-Quisquater
- Protocolo Schnorr
- Protocolo Sigma

En resumen, los sistemas de pruebas interactivos son herramientas esenciales en criptografía para verificar información sin comprometer la seguridad y privacidad de los datos.
""")

# Links de referencia
st.markdown("- [Más información sobre los SPI](https://es.wikipedia.org/wiki/Sistema_de_prueba_interactiva)")

import streamlit as st

# Título de la sección
st.title("Computación Cuántica")

# Descripción de la Computación Cuántica
st.markdown("""
La Computación Cuántica es un campo de estudio que explora el uso de principios cuánticos para procesar información de manera más eficiente que la computación clásica. Existe interés y debate sobre cómo podría afectar a la criptografía a largo plazo.

### Impacto en la Criptografía:

Se discute si la computación cuántica podría eventualmente romper algunos criptosistemas actuales al aprovechar sus capacidades únicas, como la superposición y el entrelazamiento cuántico. Sin embargo, esto es un área de investigación y existen limitaciones significativas.

### Qubits y Superposición:

Un qubit, abreviatura de quantum bit, es la unidad básica de información cuántica. A diferencia de los bits clásicos que son 0 o 1, un qubit puede estar en una superposición de ambos estados simultáneamente, lo cual es fundamental para los cálculos cuánticos.

### Ejemplo del Experimento de Doble Rendija:

El experimento de doble rendija ilustra propiedades cuánticas donde un qubit puede comportarse de manera diferente cuando no se observa. Esto podría aplicarse a resolver problemas complejos ajustando las propiedades del entorno adecuadamente.

En resumen, aunque la Computación Cuántica promete avances significativos en ciertos campos, como la optimización y simulación molecular, su impacto en la criptografía es un área de estudio en desarrollo con implicaciones aún por determinar.
""")

# Link de referencia
st.markdown("- [Más información sobre Computación Cuántica](https://es.wikipedia.org/wiki/Computaci%C3%B3n_cu%C3%A1ntica)")


import requests
from PIL import Image
from io import BytesIO
import streamlit as st

# URL de la imagen del experimento de doble rendija
image_url = "https://www.dciencia.es/wp-content/uploads/Doble-rendija1.jpg"

# Cargar la imagen desde la URL
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Agregar la imagen debajo del título
st.image(image, caption="Figura 1. Esquema del experimento de la doble rendija. A la izquierda cuando estamos observando, a la derecha cuando no estamos observando. Imagen tomada de: https://institucional.us.es/blogimus/2019/04/y-las-ondas-se-convirtieron-en-particulas/", use_column_width=True)

# URL de la imagen del qubit
image_url1 = "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*tr-EJH8iKZ5vfnGq4Iqf-w.png"

# Cargar la imagen desde la URL
response = requests.get(image_url1)
image1 = Image.open(BytesIO(response.content))

# Agregar la imagen debajo del título
st.image(image1, caption="Qubit", use_column_width=True)

# Texto estructurado como items
texto = """
- Un qubit solo puede tomar valores entre 0 y 1.
- Recopilar más información o colocar más qubits juntos puede desestabilizarlos fácilmente, requiriendo condiciones muy específicas como el aislamiento ambiental y bajas temperaturas.
- Se puede utilizar para paralelizar problemas como el cálculo del logaritmo discreto y la factorización de números primos grandes.
- Teóricamente, estas técnicas podrían romper el criptosistema RSA.
- Estudios recientes indican que se necesitan alrededor de un millón de qubits para factorizar números primos grandes.
- A este nivel, los qubits se vuelven tan inestables que es difícil mantener su coherencia en conjunto.
"""

# Mostrar en Streamlit
st.title("Problemas y aplicaciones de los qubits")
st.markdown(texto)


# """ import streamlit as st
# from PIL import Image
# import requests
# from io import BytesIO

# # URL de la imagen del circuito cuántico
# image_url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Quantum_teleportation_circuit.svg/1920px-Quantum_teleportation_circuit.svg.png"


# # Cargar la imagen desde la URL
# response = requests.get(image_url2)
# image2 = Image.open(BytesIO(response.content)) """

# # Texto para mostrar debajo de la imagen
# caption_text = """
# Circuito que realiza la teletransportación de un qubit.
# Este circuito consta tanto de puertas cuánticas como de medidas.
# La medición es un fenómeno cuántico que no ocurre en los circuitos clásicos.
# """

# # Agregar la imagen debajo del título
# st.image(image2, caption=caption_text, use_column_width=True)


st.title("Investigación en Criptografía")

# Descripción
st.write("""
Los artículos sobre criptografía más importantes que abarcan el pasado, el presente y el futuro de los criptosistemas y la criptología.
""")

import streamlit as st
from PIL import Image

# Cargar imagen desde un archivo local
#imagen_local = "math-paper1.png"
#imagen = st.image(imagen_local, caption="Non-Malleable Cryptography", use_column_width=True)


import streamlit as st

# Título
st.header("Criptografía No Maleable")

# Resumen
st.write("""
**Criptografía No Maleable**  
Danny Dolev, Cynthia Dwork y Moni Naor — Publicado en enero de 1991

"Maleable" significa capaz de transformarse en otra forma sin romperse ni agrietarse.

La no-maleabilidad, según se define en la Seguridad Semántica (Goldwasser y Micali, 1982), dice que al ver una encriptación de un mensaje, no nos ayuda a encontrar los detalles del mensaje en texto plano. El adversario no aprende nada sobre el mensaje original solo viendo la encriptación y no puede producir ningún texto plano relacionado con el mensaje.

El concepto de criptografía no maleable, una extensión de la criptografía semánticamente segura, va un paso más allá: dado el texto cifrado de un mensaje, es imposible generar un texto cifrado diferente de modo que los respectivos textos planos estén relacionados.

El mismo concepto tiene sentido en los contextos de compromiso de cadenas y pruebas de conocimiento cero. Se presentan esquemas no maleables para cada uno de estos tres problemas. Los esquemas no suponen un centro de confianza; un usuario no necesita saber nada sobre el número o la identidad de otros usuarios del sistema.

En el momento de su publicación, este criptosistema fue el primero en demostrarse seguro contra un tipo fuerte de ataque de texto cifrado elegido propuesto por Rackoff y Simon, en el que el atacante conoce el texto cifrado que desea romper y puede consultar el oráculo de descifrado sobre cualquier texto cifrado que no sea el objetivo.
""")

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/b62c499ec81e5053ef904e5c497283a2b0f056d9.pdf)")


# Cargar imagen desde un archivo local
#imagen_local2 = "math-paper2.png"
#imagen = st.image(imagen_local2, caption="On the (Im)possibility of Obfuscating Programs", use_column_width=True)

# Título
st.header("Sobre la (im)posibilidad de ofuscar programas")

# Resumen
st.write("""
**Sobre la (im)posibilidad de ofuscar programas**  
Los artículos sobre la ofuscación de programas abordan cómo hacer que un programa sea ininteligible pero funcionalmente preservado.
Esto permite que una parte entregue un programa ejecutable a otra parte sin revelar su funcionamiento interno.
La investigación comenzó en 2001 con la demostración de la imposibilidad de la ofuscación de caja negra virtual y la introducción de la ofuscación de indistinguibilidad (IO) más débil. Artículos posteriores incluyen propuestas de esquemas de IO candidatos y aplicaciones de programas perforados, resolviendo problemas como el cifrado negable y construyendo IO basado en suposiciones criptográficas.
""")

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/539a6d18a0e90fe6d9d27769b7d42469298fc329.pdf)")


##########
# Cargar imagen desde un archivo local
#imagen_local3 = "math-paper3.png"
#imagen = st.image(imagen_local2, caption="Computer Systems Established, Maintained and Trusted by Mutually Suspicious Groups", use_column_width=True)

#Titulo
st.header("Sistemas informáticos establecidos, mantenidos y en los que confían grupos mutuamente sospechosos")


# Resumen del artículo
resumen3 = """
Este artículo es la primera propuesta conocida de un protocolo de blockchain.

Chaum describe el diseño de un sistema informático distribuido que puede ser establecido, mantenido y confiable por grupos mutuamente desconfiados.

Es un sistema de registro público con consistencia de membresía grupal y cálculos de transacciones privadas que protege la privacidad individual a través de la seguridad física.

Los componentes del sistema incluyen "bóvedas" físicamente seguras, primitivas criptográficas existentes (cifrado simétrico y asimétrico, funciones hash criptográficas, firmas digitales) y una nueva primitiva introducida por Chaum: el reparto secreto umbral, donde un umbral de claves subparciales es suficiente para reconstruir la clave original.

Para más sobre la historia de las tecnologías blockchain, considere "On the Origins and Variations of Blockchain Technologies".
"""

# Mostrar el resumen en Streamlit
st.write(resumen3)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/e630610a9c7c3c8f950cfb5632b44ecf1b8926d2.pdf)")


# Cargar imagen desde un archivo local
#imagen_local4 = "math-paper4.png"
#imagen = st.image(imagen_local4, caption="A Digital Signature Based on a Conventional Encryption Function", use_column_width=True)

#Titulo
st.header("Una firma digital basada en una función de cifrado convencional")

resumen4 = """
En este artículo, Ralph C. Merkle desarrolló el concepto de los árboles de Merkle, que permiten almacenar datos eficientemente, ahorrando memoria y potencia de procesamiento.

Los árboles de Merkle utilizan funciones hash, que calculan un valor único y fijo (hash) a partir de datos. Un pequeño cambio en la entrada cambia completamente el hash; los hashes son únicos y unidireccionales. Los árboles de Merkle organizan y verifican datos mediante la creación de un árbol de hashes, donde cada nodo padre se forma a partir de los hashes de sus nodos hijos.

Los cambios en cualquier punto del árbol afectan los hashes siguientes, incluyendo el hash raíz. Las pruebas de Merkle verifican la integridad de los hashes en todas las ramas del árbol. Estos árboles son esenciales en criptomonedas como Bitcoin y Ethereum.
"""


# Mostrar el resumen en Streamlit
st.write(resumen4)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/5bcd990b11e068234c3a13b021f3266bb45a2964.pdf)")


#Titulo
st.header("La complejidad del conocimiento de los sistemas de prueba interactivos")

# Resumen del artículo sobre Zero-Knowledge Proofs
resumen5 = """
En este artículo, Shafi Goldwasser, Silvio Micali y Charles Rackoff introdujeron las pruebas de conocimiento cero (ZKP), una técnica criptográfica que permite a un probador demostrar a un verificador que un cálculo es correcto sin revelar más información que la veracidad de la declaración. Los ZKP permiten verificar la integridad de los datos sin exponer detalles subyacentes. En 2012, Goldwasser y Micali recibieron el Premio Turing por su trabajo en la teoría de la complejidad en criptografía. Una versión preliminar del artículo se publicó en 1986 y la versión revisada en 1989.
"""

# Mostrar el resumen en Streamlit
st.write(resumen5)

# Enlace al artículo
st.write("[Link al artículo](https://cdn.sanity.io/files/r000fwn3/production/0216c6a57ccda410243a2e4b165e141439d2c5ea.pdf)")