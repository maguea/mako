from enum import Enum

def new_number(reciver_number, address):
    if address[0:11] != reciver_number:
        #delete message
        return

def execute_command(msg, pnum, mako):
    cmd = msg[0]
    cmd = cmd.lower()
    cmd = cmd.split()
    if cmd[0] == "help":
        return "Help"
    if pnum == mako.admin_pnum:
        confirmation = admin_commands(cmd, mako)
    else:
        confirmation = guest_commands(cmd, mako)
    return confirmation

def error(cmd, mako):
    return "Arguments missing/unknown command"

def admin_add(cmd, mako):
    if(len(cmd) < 3):
        return error(cmd, mako)
    return "Add"

def admin_remove(cmd, mako):
    if(len(cmd) < 3):
        return error(cmd, mako)
    return "Remove"

def admin_get(cmd, mako):
    if(len(cmd) < 2):
        return error(cmd, mako)
    return "Get"

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
