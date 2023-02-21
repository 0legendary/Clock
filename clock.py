from tkinter import *

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

frame.mainloop()