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
    
def execute_command(msg, sender, mako):
    cmd = msg[0]
    cmd = cmd.lower()
    cmd = cmd.split()
    #try:
    #    if mako.contacts[sender].activation == 2:
    #        return "Please ask admin for server access"
    #except:
    #    pass
    if sender[12:22] == mako.admin_pnum:
        confirmation = admin_commands(cmd, mako)
    else:
        try : #find if phone number exists
            if cmd[0] == "help":
                return "No problem, here's the Help menu: Request, Cancel, See"
            command_dict = {
                0: guest_commands,
                1: guest_activate,
                2: guest_blocked,
            }
            commend_instructions = cmd if len(cmd) > 1 else None
            command_func = command_dict.get(mako.contacts[sender].activation, error)
            confirmation = command_func(commend_instructions, mako)
            #rewrite using a dict
            #if mako.contacts[sender].activation < 1:
            #    confirmation = guest_commands(cmd, mako)
            #elif mako.contacts[sender].activation < 2:
            #    confirmation = guest_activate(sender, cmd, mako)
            ##TO HERE
        except:
            confirmation = new_number(sender, cmd, mako)
    return confirmation

def error(cmd, mako):
    return "Arguments missing/unknown command"


##########################################################################
#Admin command below
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

def admin_block(cmd, mako):
    if cmd is None or len(cmd) > 1:
        return error(cmd, mako)
    try:
        mako.contacts[cmd[0]].activation = 0
        return f"Successfully blocked {cmd[0]}"
    except:
        return f"{cmd[0]} is not a registered user."

def admin_name(cmd, mako):
    #edit first and last name
    pass

def admin_commands(cmd, mako):
    command_dict = {
        "add": admin_add,
        "remove": admin_remove,
        "get": admin_get,
        "block": admin_block
    }
    commend_instructions = cmd[1:] if len(cmd) > 1 else None
    command_func = command_dict.get(cmd[0], error)
    return command_func(commend_instructions, mako)

##################################################################################################
#Guest funcitons below

#rename as guest
def new_number(sender, cmd, mako):
    if cmd is None or len(cmd) < 2:
        return "Please provide a valid name in the format: First Last"
    mako.contacts[sender] = contact(cmd[0], cmd[1], sender[12:23], sender, 1)
    name = cmd[0][0].upper() + cmd[0][1:]
    return f"Hello {name}, welcome to Mako. To connect and recieve infomation send Y"

#rename as guest
def guest_activate(sender, cmd, mako):
    if cmd[0] != "y":
        return "Please type Y to continue"
    new_user = mako.contacts[sender]
    confirmation = f"New user {new_user.first_name} {new_user.last_name} with the address: [{new_user.send_address}] has connected."
    print(confirmation)
    #admin_confirmation(mako, confirmation)
    mako.contacts[sender].activation = 0
    return "You are now logged as a contact on Mako. Type HELP for a list of valid commands."

def guest_blocked(sender, cmd, mako):
    return "Please ask admin for server access"

def guest_request(cmd, mako):
    return "request"

def guest_cancel(cmd, mako):
    return "cancel"

def guest_see(cmd, mako):
    return "see"

def guest_commands(sender, cmd, mako):
    print("Guest detected")
    command_dict = {
        "request": guest_request,
        "cancel": guest_cancel,
        "see": guest_see
    }
    commend_instructions = cmd[1:] if len(cmd) > 1 else None
    command_func = command_dict.get(cmd[0], error)
    return command_func(commend_instructions, mako)
