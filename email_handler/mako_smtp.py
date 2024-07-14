import smtplib
from time import sleep
from email.message import EmailMessage
import ssl

def sender_check(reciever_smtp_server, reciever_smtp_port, reciever_email, reciever_pass):
    try:
        smtp = smtplib.SMTP(reciever_smtp_server, reciever_smtp_port)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(reciever_email, reciever_pass)
        print("SMTP login successful")
        return smtp
    except:
        print("Error, invalid credentials\n") #Program will end without proper credentials

def send_response(reciever_address, return_address, mako, cmdrsp, msg):
    rsp = EmailMessage()
    rsp['From'] = reciever_address
    rsp['To'] = return_address
    rsp['Subject'] = cmdrsp
    rsp.set_content(msg[0])
    ssl_context = ssl.create_default_context()
    mako.smtp.sendmail(reciever_address, return_address, rsp.as_string())
    sleep(1)