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
