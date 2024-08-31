from datetime import datetime
#from PIL import Image
import calendar

class event:
    def __init__(self, name, month, day, year, hour, min, duration):
        self.event_name = name
        self.event_month = month
        self.event_day = day
        self.event_year = year
        self.event_hour = hour
        self.event_min = min
        self.event_duration = duration

def get_schedule(event):
    #image = Image.open('path/to/your/image.jpg')

    # Create a drawing object
    #draw = ImageDraw.Draw(image)

    # Define the square's position and size
    top_left = (50, 50)       # (x, y) coordinates for the top-left corner
    bottom_right = (150, 150) # (x, y) coordinates for the bottom-right corner

    # Draw the square
    #draw.rectangle([top_left, bottom_right], outline="red", width=5)

    #image.save('C:\Users\alexa\OneDrive\Desktop\vscode\mako\images\newimage.jpg')

def initialize_year(year):
    year_schedule = {}
    for month in range(1, 13):
        days_in_month = calendar.monthrange(year, month)[1]
        month_dict = {}
        for day in range(1, days_in_month + 1):
            month_dict[day] = {}
        year_schedule[month] = month_dict
    return year_schedule

def add_event(cmd, mako):
    pass

def request_event(event_dict, name, month, day, year, hour, min, duration):
    if hour < 11:
        return "error"
    