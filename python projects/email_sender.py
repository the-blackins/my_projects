from email.message import EmailMessage
from email_password import password
import ssl
import smtplib

email_sender = 'samichealakinyoola99@gmail.com'
email_password = password

email_reciever ='tekolon331@ippals.com'

subject = "Dont forget you have a goal to achieve"
body = """"every action you take towards your dream makes a difference"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())