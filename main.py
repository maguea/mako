# Main.py
# Matthew 4:4 "Man shall not live by bread alone, but by every word from God's mouth"

from datetime import datetime
from dotenv import load_dotenv
import os

# My libraries
from program_handler import *
from email_handler import *
from logged_chats import log

class mako_values:
    def __init__(self, log_imap, log_smtp, email, app_key, address, schedule):
        self.imap = log_imap
        self.smtp = log_smtp
        self.receiver_pnum = address[:11]
        self.reciever_email = email
        self.reciever_app_key = app_key
        self.contacts = {}
        self.admin_pnum = address[12:23]
        self.admin_address = address
        self.events = schedule

def main():
    mako = mako_input_init()
    while(mako):
        morning_call(mako)
        msg = poll(mako) #pass credentials to run program if valid
        if msg:
            for sender in msg.keys():
                command = commands.execute_command(msg[sender], sender, mako)
                history = f"From: {sender}\nTime: {msg[sender][1]}\nMessage: {msg[sender][0]}\nExecuted: {command}\n"
                log.log_cmd(history)
                print(history)
                if command == "##expo":
                    mako_smtp.send_response(sender, mako, "Spacer", "https://github.com/maguea/mako/blob/main/README.md")
                    pass
                else:
                    mako_smtp.send_response(sender, mako, "Spacer", command)

def mako_input_init():
    load_dotenv()
    
    # Get initial values
    admin_address = os.getenv("ADMIN_ADDRESS") 
    
    #get reciever information
    receiver_imap_server = "imap.gmail.com"
    receiver_smpt_server = "smtp.gmail.com"
    receiver_email = os.getenv("RECEIVER_EMAIL")
    receiver_pass = os.getenv("RECEIVER_PASS")

    #create event list
    schedule = {}
    schedule[2024] = events.initialize_year(2024)

    # Login using given credentials
    imap = mako_imap.reciever_check(receiver_imap_server, receiver_email, receiver_pass)
    smtp = mako_smtp.sender_check(receiver_smpt_server, 587, receiver_email, receiver_pass)

    if not imap or not smtp:
        return  
    return mako_values(imap, smtp, receiver_email, receiver_pass, admin_address, schedule)

#Checks for new messages
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
    
def morning_call(mako):
    now = datetime.now()
    current_hour = now.hour
    current_minutes = now.minute
    current_seconds = now.second
    if current_hour == 8 and current_minutes == 00 and current_seconds < 1:
        commands.admin_confirmation(mako, str(now))

if __name__ == '__main__':
    main()