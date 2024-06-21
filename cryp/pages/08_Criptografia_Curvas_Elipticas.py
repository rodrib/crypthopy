import streamlit as st
from PIL import Image
import requests

# Título de la aplicación
st.title("Criptografía de Curva Elíptica (ECC)")

# Imagen relacionada con criptografía
image_url = "https://www.fortinet.com/content/fortinet-com/zh_tw/resources/cyberglossary/what-is-cryptography/_jcr_content/par/c05_container_copy_c/par/c28_image_copy_copy.img.jpg/1701209624270.jpg"
image = Image.open(requests.get(image_url, stream=True).raw)
st.image(image, caption="Criptografía", use_column_width=True)

# Sección de Introducción
st.header("Introducción")
st.write("""
La criptografía de curva elíptica (ECC) es una forma potente de criptografía moderna, que permite obtener claves públicas y privadas para compartir y proteger secretos de manera segura. ECC es reconocida por su alta eficiencia, rapidez y escalabilidad, lo que la hace ideal para su uso en tecnologías como blockchain, garantizando una altísima seguridad.
""")

# Sección: ¿Qué es la Criptografía de Curva Elíptica (ECC)?
st.header("¿Qué es la Criptografía de Curva Elíptica (ECC)?")
st.write("""
La criptografía de curva elíptica (ECC) es un método de cifrado asimétrico que utiliza estructuras algebraicas de curvas elípticas sobre campos finitos. Esto permite que las claves sean más pequeñas en comparación con otros sistemas criptográficos, sin comprometer la seguridad. La ECC es ampliamente utilizada en acuerdos de claves, firmas digitales y generadores pseudoaleatorios, además de combinarse con cifrados simétricos para mayor protección. Su seguridad se basa en la dificultad de resolver el problema de logaritmo discreto de curva elíptica (ECDLP).
""")

# Sección: Historia de la ECC
st.header("Historia de la ECC")
st.write("""
La criptografía basada en curvas elípticas fue propuesta en la década de 1980 por Victor Miller y Neal Koblitz, destacando sus propiedades matemáticas para aplicaciones criptográficas seguras. Desde entonces, la ECC ha soportado múltiples ataques y se ha normalizado por estándares como ANSI, NIST y FIPS, demostrando su confiabilidad y aplicabilidad en empresas y dispositivos inalámbricos donde la seguridad es vital.
""")

# Sección: ¿Cómo funciona la ECC?
st.header("¿Cómo funciona la ECC?")
st.write("""
Los algoritmos ECC, como el Algoritmo de Firma Digital de Curva Elíptica (ECDSA), utilizan coordenadas en una curva elíptica en lugar de números primos, como en el RSA. Una curva elíptica se representa algebraicamente con la ecuación:
""")
st.latex(r'''y^2 = x^3 + ax + b''')
st.write("""
Dependiendo de los valores de a y b, las curvas elípticas toman diferentes formas. En el caso de Bitcoin, se utiliza una curva elíptica ECDSA con la curva secp256k1.
""")
