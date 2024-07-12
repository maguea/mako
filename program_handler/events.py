from datetime import datetime

class event:
    def __init__(self, name, month, day, year, hour, min, duration):
        self.event_name = name
        self.event_month = month
        self.event_day = day
        self.event_year = year
        self.event_hour = hour
        self.event_min = min
        self.event_duration = duration

def add_event(event_dict, name, month, day, year, hour, min, duration):

    pass

def request_event(event_dict, name, month, day, year, hour, min, duration):
    if(hour < 11):
        return "error"

meeting = event("meeting", 7, 12, 2024, 15, 20, 2)

nottime = True
while(nottime):
    now = datetime.now()
    if(now.hour == meeting.event_hour and now.minute == meeting.event_min ):
        print("Meeting time")
        nottime = False