import smtplib,ssl
import os

USERNAME="aviral18@gmail.com"
#remember to run script as admin/main user
PASSWORD=os.getenv("PASSWORD")      #get value from PASSWORD environment variable declared

def send_email(message):

    host="smtp.gmail.com"
    port = 465
    username=USERNAME
    password=PASSWORD

    context=ssl.create_default_context()
    receiver="aviral18@gmail.com"             #

    #message="""\
    #Subject: Hola
    #I Love You
    #:*
    #"""

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)
