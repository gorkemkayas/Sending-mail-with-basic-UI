import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
import sys


class Mail_sending():
    checking = "Empty"
    def __init__(self,mail_address,mail_password,mail_receiver,mail_subject,mail_content):
        self.mail_address = mail_address
        self.mail_password = mail_password
        self.mail_receiver = mail_receiver
        self.mail_subject = mail_subject
        self.mail_content = mail_content

        message = MIMEMultipart()

        message["From"] = formataddr((str(Header("gorkidev mail application","utf-8")),self.mail_address))
        message["To"] = ("{}".format(self.mail_receiver))
        message["Subject"] = self.mail_subject

        content = self.mail_content

        formed_content = MIMEText(content,"plain")

        message.attach(formed_content)

        try:
            print("Burda mı 1")
            mail_connection = smtplib.SMTP("smtp.gmail.com",587)
            print("Burda mı 2")
            mail_connection.ehlo()
            mail_connection.starttls()
            print("Burda mı 3")
            mail_connection.login(self.mail_address,self.mail_password)
            print("Burda mı 4")
            mail_connection.sendmail(message["From"],message["To"],message.as_string())
            print("Burda mı 5")

            print("Mail is sended successfully! ")
            self.checking = "True"


        except:
            sys.stderr.write("There is an error!")
            sys.stderr.flush()
            self.checking = "False"

        print(self.checking)



my_mail = Mail_sending("gorkemkayas435@gmail.com","duvwcssiyyqtbnzz","gorkemkayas@hotmail.com","baslık deneme","content deneme")