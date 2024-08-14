# Main.py
# Matthew 4:4 "Man shall not live by bread alone, but by every word from God's mouth"

from datetime import datetime

# My libraries
from program_handler import *
from email_handler import *

class mako_values:
    def __init__(self, log_imap, log_smtp, pnum, adddress, email, app_key, admin_pnum, schedule):
        self.imap = log_imap
        self.smtp = log_smtp
        self.receiver_pnum = pnum
        self.reciever_email = email
        self.reciever_app_key = app_key
        self.contacts = {}
        self.admin_pnum = admin_pnum
        self.admin_address = adddress
        self.events = schedule
        self.month = datetime.now().month 
        self.day = datetime.now().day      
        self.year = datetime.now().year

def main():
    mako = mako_input_init()
    t = True
    while(t):
        msg = poll(mako) #pass credentials to run program if valid
        if msg:
            for sender in msg.keys():
                command = commands.execute_command(msg[sender], sender, mako)
                print(command)
                mako_smtp.send_response(sender, mako, "Spacer", command)

def mako_input_init():
    # Get initial values
    admin_pnum = input("Enter admin phone number: ")
    admin_address = input("Enter admin return address: ")

    #get reciever information
    receiver_pnum = input("Enter receiver phone number: ")
    receiver_imap_server = input("Enter receiver IMAP server: ")
    receiver_smpt_server = input("Enter receiver SMTP server: ")
    receiver_email = input("Enter receiver email address: ")
    receiver_pass = input("Enter receiver app key: ")

    #create event list
    schedule = {}
    schedule[2024] = events.initialize_year(2024)
    print(schedule[2024][int(1)])

    # Login using given credentials
    imap = mako_imap.reciever_check(receiver_imap_server, receiver_email, receiver_pass)
    smtp = mako_smtp.sender_check(receiver_smpt_server, 587, receiver_email, receiver_pass)

    if not imap or not smtp:
        return  
    return mako_values(imap, smtp, receiver_pnum, receiver_email, receiver_pass, admin_pnum, admin_address, schedule)

def poll(mako):
    mako.imap.select("Inbox")
    _, msgnums = mako.imap.search(None, "ALL")
    countcheck = str(msgnums[0])
    countcheck = mako_imap.get_msg_count(countcheck)
    current_time = datetime.now()
    current_time = current_time.strftime("%m/%d/%Y %H:%M:%S")
    if countcheck > 0:
        msg = mako_imap.reciever_read(mako.imap, mako.receiver_pnum)
        for sender in msg.keys():
            msg[sender] = [msg[sender], current_time]
        return msg

if __name__ == '__main__':
    main()