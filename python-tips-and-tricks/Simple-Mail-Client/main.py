from email.mime import text
import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.world4you.com', 25)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('mailtesting@neuralnine.com', password)

msg = MIMEMultipart()
msg['From'] = 'neuralnine'
msg['To'] = 'mailtesting@spaml.de'
msg['Subject'] = 'just a test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('mailtesting@neuralnine.com', 'mailtesting@spaml.de', text)