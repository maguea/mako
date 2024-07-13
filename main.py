#main
# Matthew 4:4 "Man shall not live by bread alone, but by every word from God's mouth"
from time import sleep
from datetime import date

#mine
from program_handler import *
from email_handler import*

def main():
    # Get initial values
    #admin_pnum = input("Enter admin phone number: ")
    #admin_name = input("Enter admin first and last name: ")
    #admin_address = input("Enter admin address")

    reciver_pnum = input("Enter reciever phone number: ")
    reciever_imap_server = input("Enter reciver IMAP server: ")
    reciever_email = input("Enter reciever email address: ")
    reciver_pass = input("Enter reciever app key: ")

    #create admin credintials
    #admin_names = admin_name.split()
    #admin_contact = contacts.contact(admin_names[0], admin_names[1], admin_pnum, admin_address, 0)
    #contact_list = { admin_pnum: admin_contact }

    #create event list

    # Login using given credentials
    imap = mako_imap.reciever_check(reciever_imap_server, reciever_email, reciver_pass)
    if imap:
        poll(imap, reciver_pnum) #pass credentials to run program if valid
    return   

def poll(imap, reciver_pnum):
    f=True
    count = 0
    while(f):
        imap.select("Inbox")
        _, msgnums = imap.search(None, "ALL")
        countcheck = str(msgnums[0])
        if int(countcheck[-2]) > count:
            count = int(countcheck[-2])
            #current_time = datetime.now()
            msg = mako_imap.reciever_read(imap, reciver_pnum)
            print(msg)
            #print(current_time)
            sleep(1)

main()