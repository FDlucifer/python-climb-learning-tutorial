import csv
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = "1185151867@qq.com"
email_password = "" # here put your email password in
subject = "subscription activated"

with open('emails.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        text = "hello " + line[1] + " your " + line[2] + " plan has been activated "
        # print(text)
        email_send = line[0]
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.attach(MIMEText(text, "plain"))
        text = msg.as_string()

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email_user, email_password)
        server.sendmail(email_user, email_send, text)

        server.quit()
