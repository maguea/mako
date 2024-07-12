import imaplib, email

def reciever_login(imap_server, reciever_email, reciever_pass):
    try:
        imap = imaplib.IMAP4_SSL(imap_server)
        imap.login(reciever_email, reciever_pass)
        reciever_read(imap)
    except:
        print("Error, invalid credentials")

def reciever_read(imap):
    imap.select("Inbox")

