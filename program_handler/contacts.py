from enum import Enum

class clearance(Enum):
    admin = 0
    guest = 1
    block = 2

class contact():
    def __init__(self, first_name, last_name, pnum, address, clearance):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = pnum
        self.send_address = address
        self.clearance = clearance