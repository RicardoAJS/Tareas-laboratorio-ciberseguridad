from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json

import sys

if len(sys.argv) == 1:
	print("ingresa el mensaje a enviar")

data = {}
with open ('datos.json') as f :
    data = json.load(f)

msg = MIMEMultipart()

message = "sys.argv[1] 

msg['From'] = data['user']

receipents = ["ricardo.jacobosjn@uanl.edu.mx"]

msg['To'] = ", ".join(receipents)

msg ['Subject'] = "Hola Hermano"

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.office365.com:587')

server.starttls()

server.login(data['user'], data['pass'])

server.sendmail(msg['From'], receipents, msg.as_string())


server.quit()

print("Email enviado con exito")



    
