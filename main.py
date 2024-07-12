#main

# Matthew 4:4 "Man shall not live by bread alone, but by every word from God's mouth"

import getpass

#mine
from program_handler import *
from email_handler import*

def initialize():
    # Get initial values
    admin_pnum = input("Enter admin phone number: ")
    admin_name = input("Enter admin first and last name: ")
    admin_address = input("Enter admin address")

    reciver_pnum = input("Enter reciever phone number: ")
    reciever_imap_server = input("Enter reciver IMAP server: ")
    reciever_email = input("Enter reciever email address: ")
    reciver_pass = getpass()

    #create admin credintials
    admin_names = admin_name.split()
    admin_contact = contacts.contact(admin_names[0], admin_names[1], admin_pnum, admin_address, 0)
    contact_list = { admin_pnum: admin_contact }

    imap.reciever_login(reciever_imap_server, reciever_email, reciver_pass)

