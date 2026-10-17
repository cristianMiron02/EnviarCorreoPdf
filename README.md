
# PDF to Email - Python

Aplicación desarrollada en Python que permite extraer texto de documentos PDF y enviarlo automáticamente por correo electrónico, incluyendo el documento original como archivo adjunto.

El objetivo de este proyecto es facilitar la automatización del procesamiento y envío de documentos digitales.

## Características

- Extracción de texto de archivos PDF.
- Lectura de documentos con múltiples páginas.
- Envío automático de correos electrónicos mediante SMTP.
- Inclusión del texto extraído en el cuerpo del correo.
- Envío del archivo PDF original como adjunto.
- Configuración de credenciales mediante variables de entorno.
- Gestión básica de errores.
- Compatible con Windows, Linux y macOS.

## Tecnologías utilizadas

- Python 3
- PyMuPDF (fitz)
- smtplib
- email.message
- os
- pathlib

## Estructura del proyecto

```text
python-pdf-email/
├── enviar_pdf.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/python-pdf-email.git
```

### 2. Acceder al directorio

```bash
cd python-pdf-email
```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

El archivo `requirements.txt` debe contener:

```text
pymupdf
```

## Configuración

El programa utiliza Gmail como servidor SMTP.

Para utilizarlo es necesario disponer de una cuenta de Gmail con la verificación en dos pasos activada y generar una contraseña de aplicación.

### Windows (PowerShell)

```powershell
$env:EMAIL_USER="tu_correo@gmail.com"
$env:EMAIL_PASSWORD="tu_contraseña_de_aplicacion"
```

### Linux y macOS

```bash
export EMAIL_USER="tu_correo@gmail.com"
export EMAIL_PASSWORD="tu_contraseña_de_aplicacion"
```

Las credenciales no deben incluirse directamente en el código fuente ni publicarse en GitHub.

## Uso

### 1. Preparar el documento

Coloca el archivo PDF que deseas procesar en el directorio del proyecto.

### 2. Configurar el destinatario

Abre `enviar_pdf.py` y modifica las siguientes variables:

```python
ruta_pdf = "documento.pdf"
destinatario = "destinatario@ejemplo.com"
```

### 3. Ejecutar el programa

```bash
python enviar_pdf.py
```

Si el proceso se completa correctamente, aparecerá el siguiente mensaje:

```text
Correo enviado correctamente.
```

El destinatario recibirá el texto extraído del PDF en el cuerpo del correo y el documento original como archivo adjunto.

## Funcionamiento

El programa realiza las siguientes operaciones:

1. Abre el archivo PDF mediante PyMuPDF.
2. Recorre todas las páginas del documento.
3. Extrae el texto de cada página.
4. Genera un mensaje de correo electrónico.
5. Añade el texto extraído al cuerpo del mensaje.
6. Adjunta el archivo PDF original.
7. Establece una conexión segura con el servidor SMTP de Gmail.
8. Envía el correo al destinatario configurado.

## Seguridad

El proyecto utiliza variables de entorno para gestionar las credenciales de acceso.

Se recomienda:

- No almacenar contraseñas en el código fuente.
- Utilizar contraseñas de aplicación.
- Mantener los archivos de configuración privados fuera del repositorio.
- No publicar documentos PDF que contengan información confidencial.
- Revisar los destinatarios antes de ejecutar el envío.

## Limitaciones

- No permite extraer texto de documentos escaneados sin utilizar OCR.
- La configuración inicial está preparada para Gmail.
- Requiere conexión a Internet.
- El tamaño máximo de los correos depende del proveedor.
- No dispone de interfaz gráfica en la versión inicial.
- Los documentos PDF sin texto extraíble no se procesan.

Proyecto desarrollado en Python como herramienta para automatizar tareas relacionadas con la gestión y el envío de documentos digitales.
