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
minute_hand_length = radius * 0.6
hour_hand_length = radius * 0.5

# Needle config
second_hand = circle.create_line(0, 0, 0, 0, width=2, fill='red')

minute_hand = circle.create_line(0, 0, 0, 0, width=4, fill='blue')

hour_hand = circle.create_line(0, 0, 0, 0, width=4, fill='black')

frame.mainloop()