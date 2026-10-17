import os
import smtplib
from pathlib import Path
from email.message import EmailMessage

import fitz  # PyMuPDF


def extraer_texto_pdf(ruta_pdf):
    """Extrae el texto de todas las páginas del PDF."""
    texto = []

    with fitz.open(ruta_pdf) as documento:
        for numero, pagina in enumerate(documento, start=1):
            contenido = pagina.get_text("text")
            texto.append(f"\n--- Página {numero} ---\n{contenido}")

    return "\n".join(texto)


def enviar_correo(destinatario, asunto, texto, ruta_pdf):
    """Envía un correo con el texto extraído y el PDF adjunto."""

    remitente = os.environ["EMAIL_USER"]
    password = os.environ["EMAIL_PASSWORD"]

    mensaje = EmailMessage()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto

    mensaje.set_content(
        "Texto extraído del documento PDF:\n\n" + texto
    )

    # Adjuntar PDF original
    with open(ruta_pdf, "rb") as archivo:
        mensaje.add_attachment(
            archivo.read(),
            maintype="application",
            subtype="pdf",
            filename=Path(ruta_pdf).name
        )

    # Conectar con Gmail mediante SSL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remitente, password)
        servidor.send_message(mensaje)

    print("Correo enviado correctamente.")


if __name__ == "__main__":
    ruta_pdf = "documento.pdf"
    destinatario = "destinatario@ejemplo.com"

    try:
        texto = extraer_texto_pdf(ruta_pdf)

        if not texto.strip():
            print("El PDF no contiene texto extraíble.")
        else:
            enviar_correo(
                destinatario=destinatario,
                asunto="Contenido del documento PDF",
                texto=texto,
                ruta_pdf=ruta_pdf
            )

    except Exception as error:
        print(f"Error: {error}")
