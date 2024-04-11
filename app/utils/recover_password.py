import os
import smtplib
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

def change_password(user_email, confirmation_link):
    # Configuración del servidor de correo
    smtp_server = os.getenv('EMAIL_SERVER')
    smtp_port = os.getenv('EMAIL_PORT')
    smtp_username = os.getenv('EMAIL_USERNAME')
    smtp_password = os.getenv('EMAIL_PASSWORD')

    # Creación del mensaje
    msg = MIMEMultipart()
    msg['From'] = smtp_server
    msg['To'] = user_email
    msg['Subject'] = "Confirmación de cuenta"

    # Leer el archivo HTML
    with open('app/assets/html/change_password.html', 'r') as f:
        html_content = f.read()

    # Reemplazar un marcador de posición en el HTML con el enlace de confirmación
    html_content = html_content.replace('{confirmation_link}', confirmation_link)

    # Crear el cuerpo del mensaje con el contenido HTML
    msg.attach(MIMEText(html_content, 'html'))

    # Conexión al servidor de correo y envío del mensaje
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    text = msg.as_string()
    server.sendmail(smtp_username, user_email, text)
    server.quit()




