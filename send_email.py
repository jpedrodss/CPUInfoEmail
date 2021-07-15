from memory_info import print_memory_values
from network_info import print_network_info
from disk_usage import print_disk_usage
from email.message import EmailMessage
from cpu_info import print_cpu_values
from dotenv import load_dotenv
import smtplib
import os

# Carrega as informações do .env
load_dotenv()

def send_email():
    # Define email de origem e destino
    me = 'jpedrodss@gmail.com'
    you = 'ls.sampaio@outlook.com'

    # gustavo.mainchein@darede.com.br

    # Define tipo do email
    msg = EmailMessage()

    # Define mensagem do email
    message = print_cpu_values() + print_network_info() + \
        print_memory_values() + print_disk_usage()

    msg.set_content(message)
    # Define o assunto do email
    # subject = 'Informações da máquina'

    # Senha do email de origem
    password = os.getenv('gmail_password')

    # Origem do email
    msg['From'] = me
    # Destino do email
    msg['To'] = you
    # Assunto do email
    msg['Subject'] = 'Informações da máquina'

    # Define o servidor de onde será enviado o email
    server = smtplib.SMTP('smtp.gmail.com: 587')
    # Inicia o servidor
    server.starttls()

    # Faz o login no email de origem
    server.login(me, password)

    # Envia o email
    server.sendmail(me, you, msg.as_string())
    server.quit()

send_email()
