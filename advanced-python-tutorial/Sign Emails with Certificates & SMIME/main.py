# openssl genrsa -out private_key.pem 2048
# openssl req -new -key private_key.pem -out csr.pem
# openssl x509 -req -in csr.pem -signkey private_key.pem -out certificate.pem -days 365
# pip install python-smail

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smail import sign_message

LOGIN_MAIL, LOGIN_PASS = open("LOGIN_INFO", "r").read().split("\n")
SMTP_SERVER = "smtp.web.de"
SMTP_PORT = 587

CERT_FILE = "certs/certificate.pem"
KEY_FILE = "certs/private_key.pem"

recipient = "accounts@luci11.com"
message = """hello,
this email will be signed!
hope you are excited!"""

msg = MIMEMultipart("related")
msg.attach(MIMEText(message, "plain", _charset="UTF-8"))
msg['Subject'] = "My Signed Message"
msg['From'] = LOGIN_MAIL
msg['To'] = recipient

signed_msg = sign_message(msg, KEY_FILE, CERT_FILE)

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(LOGIN_MAIL, LOGIN_PASS)
    server.send_message(signed_msg)

print("e-mail was sent successfully!")
