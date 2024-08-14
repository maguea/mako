# Commands.py
from enum import Enum
from email_handler import mako_smtp

class clearance(Enum):
    admin = 0
    guest = 1

class activation(Enum):
    active = 0
    inactive = 1
    blocked = 2

class contact():
    def __init__(self, first_name, last_name, pnum, address, clearance):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = pnum
        self.send_address = address
        self.clearance = clearance
        self.activation = 1

def new_number(sender, cmd, mako):
    print(cmd)
    if cmd is None or len(cmd) < 2:
        return "Please provide a valid name in the format: First Last"
    mako.contacts[sender] = contact(cmd[0], cmd[1], sender[12:23], sender, 1)
    return "Hello, welcome to Mako. To connect and recieve infomation send Y"

def activate_number(sender, msg, mako):
    print(msg[0] == "y")
    if msg[0] != "y":
        return "Please type Y to continue"
    new_user = mako.contacts[sender]
    confirmation = f"New user {new_user.first_name} {new_user.last_name} with the address: [{new_user.send_address}] has connected."
    #admin_confirmation(mako, confirmation)
    mako.contacts[sender].activation = 0
    return "Welcome to Mako. Type HELP for a list of valid commands."
    

def execute_command(msg, sender, mako):
    cmd = msg[0]
    cmd = cmd.lower()
    cmd = cmd.split()
    if cmd[0] == "help":
        return "No problem, here's the Help menu:\nRequest\nRemove\nGet"
    if sender[12:22] == mako.admin_pnum:
        confirmation = admin_commands(cmd, mako)
    else:
        try : #find if phone number exists
            if mako.contacts[sender].activation < 1:
                confirmation = guest_commands(cmd, mako)
            else:
                confirmation = activate_number(sender, cmd, mako)
        except:
            confirmation = new_number(sender, cmd, mako)
    return confirmation

def error(cmd, mako):
    return "Arguments missing/unknown command"

def admin_confirmation(mako, msg):
    mako_smtp.send_response(mako.admin_address, mako, "Spacer", msg)

def admin_add(cmd, mako):
    if cmd is None or len(cmd) < 3:
        return error(cmd, mako)
    elif mako.month < cmd[0] and (mako.year <= cmd[2] and mako.year % 100 <= cmd[2]):
        return "Invalid date"
    try:
        print(mako.events[int(cmd[2])][int(cmd[0])])
        return "Add"
    except:
        return "Invalid date"

def admin_remove(cmd, mako):
    if cmd is None or len(cmd) < 3:
        return error(cmd, mako)
    return "Remove"

def admin_get(cmd, mako):
    if cmd is None or len(cmd) < 2:
        return error(cmd, mako)
    return "Get"

def admin_update(cmd, mako):
    pass

def admin_commands(cmd, mako):
    print("Admin detected")
    command_dict = {
        "add": admin_add,
        "remove": admin_remove,
        "get": admin_get
    }
    commend_instructions = cmd[1:] if len(cmd) > 1 else None
    command_func = command_dict.get(cmd[0], error)
    return command_func(commend_instructions, mako)

def guest_request(cmd, mako):
    return "request"

def guest_cancel(cmd, mako):
    return "cancel"

def guest_see(cmd, mako):
    return "see"

def guest_commands(cmd, mako):
    print("Guest detected")
    command_dict = {
        "request": guest_request,
        "cancel": guest_cancel,
        "see": guest_see
    }

    commend_instructions = cmd[1:] if len(cmd) > 1 else None
    command_func = command_dict.get(cmd[0], error)
    return command_func(commend_instructions, mako)
