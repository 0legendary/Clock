from tkinter import *
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
second_hand_length = radius * 0.8
minute_hand_length = radius * 0.9
hour_hand_length = radius * 0.5

# Needle config
second_hand = circle.create_line(0, 0, 0, 0, width=2, fill='red')

minute_hand = circle.create_line(0, 0, 0, 0, width=4, fill='blue')

hour_hand = circle.create_line(0, 0, 0, 0, width=4, fill='black')


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


update_clock()

frame.mainloop()
