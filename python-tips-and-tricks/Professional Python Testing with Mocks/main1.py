import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import unittest
from unittest.mock import patch, ANY

def send_email(smtp_server, smtp_port, from_addr, to_addr, subject, body):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_addr, "MyPassword")
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

class TestEmail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_send_mail(self, mock_smtp):
        instance = mock_smtp.return_value
        send_email("smtp.example.com", 587, "mymail@example.com", "hismail@example.com", "Subject", "Mail Contents")

        mock_smtp.assert_called_with("smtp.example.com", 587)

        instance.starttls.assert_called_with()
        instance.login.assert_called_with("mymail@example.com", "MyPassword")
        instance.sendmail.assert_called_with("mymail@example.com", "hismail@example.com", ANY)
        instance.quit.assert_called_with()

if __name__ == "__main__":
    unittest.main()
