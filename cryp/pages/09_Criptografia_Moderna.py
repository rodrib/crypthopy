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


import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# URL de la imagen del circuito cuántico
image_url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Quantum_teleportation_circuit.svg/1920px-Quantum_teleportation_circuit.svg.png"


# Cargar la imagen desde la URL
response = requests.get(image_url2)
image2 = Image.open(BytesIO(response.content))

# Texto para mostrar debajo de la imagen
caption_text = """
Circuito que realiza la teletransportación de un qubit.
Este circuito consta tanto de puertas cuánticas como de medidas.
La medición es un fenómeno cuántico que no ocurre en los circuitos clásicos.
"""

# Agregar la imagen debajo del título
st.image(image2, caption=caption_text, use_column_width=True)