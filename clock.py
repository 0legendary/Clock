from tkinter import *
import datetime
import math
import time

# Creating a window with adjustment
frame = Tk()
frame.title("CLOCK")
frame.geometry('1920x1080')
frame.config(bg='grey18')

# Creating a circle
circle = Canvas(frame, width=1000, height=1000, highlightthickness=1, bg='grey18')
circle.pack()

# Center the circle
center_x = 1000 / 2
center_y = 1000 / 2

radius = 350
point_radius = 5
circle.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                   outline='grey32', width=8, )

# Needles of the clock (length)
second_hand_length = radius * 0.9
minute_hand_length = radius * 0.7
hour_hand_length = radius * 0.5

# Needle config
hour_hand = circle.create_line(0, 0, 0, 0, width=10, fill='black', capstyle='round')

minute_hand = circle.create_line(0, 0, 0, 0, width=6, fill='black', capstyle='round')

second_hand = circle.create_line(0, 0, 0, 0, width=2, fill='red', capstyle='projecting', joinstyle='bevel')

for hour in range(1, 60):
    angle = math.radians(hour * 6)  # there are 60 min on a clock, so 360 / 60 = 6 degrees per hour

    x1 = center_x + (radius - 10) * math.sin(angle)
    y1 = center_y - (radius - 10) * math.cos(angle)
    x2 = center_x + radius * math.sin(angle)
    y2 = center_y - radius * math.cos(angle)

    # minute marker line
    circle.create_line(x1, y1, x2, y2, width=2, fill='grey12')

for hour in range(1, 13):
    angle = math.radians(hour * 30)  # there are 12 hours on a clock, so 360 / 12 = 30 degrees per hour

    x1 = center_x + (radius - 10) * math.sin(angle)
    y1 = center_y - (radius - 10) * math.cos(angle)
    x2 = center_x + radius * math.sin(angle)
    y2 = center_y - radius * math.cos(angle)

    # hour marker line
    circle.create_line(x1, y1, x2, y2, width=4, fill='black')


def update_clock():
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    hours = current_time.tm_hour

    second_hand_angle = (math.pi / 30) * seconds
    minute_hand_angle = (math.pi / 30) * minutes + (math.pi / 1800) * seconds

    hour_hand_angle = ((30 * (hours % 12)) + (0.5 * minutes) + (0.5 / 60 * seconds)) * math.pi / 180

    # second hand coordination
    second_hand_x = center_x + second_hand_length * math.sin(second_hand_angle)
    second_hand_y = center_y - second_hand_length * math.cos(second_hand_angle)

    # minute hand coordination
    minute_hand_x = center_x + minute_hand_length * math.sin(minute_hand_angle)
    minute_hand_y = center_y - minute_hand_length * math.cos(minute_hand_angle)

    # hour hand coordination
    hour_hand_x = center_x + hour_hand_length * math.sin(hour_hand_angle)
    hour_hand_y = center_y - hour_hand_length * math.cos(hour_hand_angle)

    circle.coords(second_hand, center_x, center_y, second_hand_x, second_hand_y)
    circle.coords(minute_hand, center_x, center_y, minute_hand_x, minute_hand_y)
    circle.coords(hour_hand, center_x, center_y, hour_hand_x, hour_hand_y)

    circle.after(10, update_clock)


time_label = Label(circle, font=('FreeMono', 18))
date_label = Label(circle, font=('FreeMono', 18))


def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time, bg='grey18', foreground="grey71", )
    time_label.after(1000, update_time)  # to update every second
    time_label.place(relx=.87, rely=.95)


def update_date():
    current_date = datetime.date.today()
    date_format = current_date.strftime('%d:%m:%Y')
    date_label.config(text=date_format, bg='grey18', foreground="black")
    date_label.after(1000, update_date)  # to update every second
    date_label.place(relx=.85, rely=.01)


update_date()
update_time()
update_clock()

frame.mainloop()
