
def execute_command(msg, user):
    msg.lower()
    cmd = msg.split()
    if cmd[0] == "help":
        print("Help")
    if user == "admin":
        confirmation = admin_commands(cmd)
    else:
        confirmation = guest_commands(cmd)
    print(confirmation)

def new_number(reciver_number, address):
    if address[0:11] != reciver_number:
        #delete message
        return
    
    pass

def error(cmd):
    return "Command not recognized"

def admin_add(cmd):
    return "add"

def admin_remove(cmd):
    return "remove"

def admin_get(cmd):
    return "get"

def admin_commands(cmd):
    print("Admin detected")
    command_dict = {
        "add": admin_add,
        "remove": admin_remove,
        "get": admin_get
    }

    commend_instructions = cmd[1:] if len(cmd) > 1 else None
    command_func = command_dict.get(cmd[0], error)
    return command_func(commend_instructions)

def guest_request(cmd):
    return "request"

def guest_cancel(cmd):
    return "cancel"

def guest_see(cmd):
    return "see"

def guest_commands(cmd):
    print("Guest detected")

    command_dict = {
        "request": guest_request,
        "cancel": guest_cancel,
        "see": guest_see
    }

    commend_instructions = cmd[1:] if len(cmd) > 1 else None
    command_func = command_dict.get(cmd[0], error)
    return command_func(commend_instructions)
