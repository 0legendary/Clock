from tkinter import *
from tkinter import Entry

window = Tk()
window.title("Calculator")
window.geometry('700x750')
window.config(bg="gray")
window.eval('tk::PlaceWindow . center')

def button_click(number):
    current = box.get()     # To enter thr number correct way as we need
    box.delete(0, END)
    box.insert(0, str(current) + str(number))  # To insert a number to display

def button_clear():
     box.delete(0, END)

def button_add():
    first_number = box.get()
    global f_num
    global math
    math = "Addition"
    f_num = float(first_number)
    box.delete(0, END)

def button_mult():
    first_number = box.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = float(first_number)
    box.delete(0, END)

def button_div():
    first_number = box.get()
    global f_num
    global math
    math = "Division"
    f_num = float(first_number)
    box.delete(0, END)


def button_subtract():
    first_number = box.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = float(first_number)
    box.delete(0, END)


def button_equal():
    second_number = box.get()
    box.delete(0, END)
    if math == "Addition":
        box.insert(0, f_num + float(second_number))
    if math == "Subtraction":
        box.insert(0, f_num - float(second_number))
    if math == "Division":
        box.insert(0, f_num / float(second_number))
    if math == "Multiplication":
        box.insert(0, f_num * float(second_number))


box: Entry = Entry(window, width=74, font=('Arial', 12), justify=RIGHT)
box.grid(row=0, columnspan=5, padx=0, pady=50, ipadx=0, ipady=20 )
box.place(relx=0.32, rely=0.29, height=60)

button7 = Button(text="7", height=7, width=13, foreground='red', command=lambda: button_click(7))
button7.grid(row=7, column=0, padx=5, pady=5)
button7.place(relx=0.32, rely=0.385)

button8 = Button(text="8", height=7, width=13, foreground='red', command=lambda: button_click(8))
button8.grid(row=7, column=1, padx=5, pady=5)
button8.place(relx=0.39, rely=0.385)

button9 = Button(text="9", height=7, width=13, foreground='red', command=lambda: button_click(9))
button9.grid(row=7, column=2, padx=5, pady=5)
button9.place(relx=0.46, rely=0.385)

button6 = Button(text="6", height=7, width=13, foreground='red', command=lambda: button_click(6))
button6.grid(row=8, column=2, padx=5, pady=5)
button6.place(relx=0.46, rely=0.530)

button5 = Button(text="5", height=7, width=13, foreground='red', command=lambda: button_click(5))
button5.grid(row=8, column=1, padx=5, pady=5)
button5.place(relx=0.39, rely=0.530)

button4 = Button(text="4", height=7, width=13, foreground='red', command=lambda: button_click(4))
button4.grid(row=8, column=0, padx=5, pady=5)
button4.place(relx=0.32, rely=0.530)

button3 = Button(text="3", height=7, width=13, foreground='red', command=lambda: button_click(3))
button3.grid(row=9, column=2, padx=5, pady=5)
button3.place(relx=0.46, rely=0.675)

button2 = Button(text="2", height=7, width=13, foreground='red', command=lambda: button_click(2))
button2.grid(row=9, column=1, padx=5, pady=5)
button2.place(relx=0.39, rely=0.675)

button1 = Button(text="1", height=7, width=13, foreground='red', command=lambda: button_click(1))
button1.grid(row=9, column=0, padx=5, pady=5)
button1.place(relx=0.32, rely=0.675)

button_dot = Button(text=".", height=7, width=13, foreground='red', command=lambda: button_click("."))
button_dot.grid(row=10, column=0, padx=5, pady=5)
button_dot.place(relx=0.32, rely=0.82)

button0 = Button(text="0", height=7, width=13, foreground='red', command=lambda: button_click(0))
button0.grid(row=10, column=1, padx=5, pady=5)
button0.place(relx=0.39, rely=0.82)

button_equal = Button(text="=", height=7, width=30, command=button_equal)
button_equal.grid(row=10, column=2, columnspan=2, padx=5, pady=5)
button_equal.place(relx=0.46, rely=0.82)

button_plus = Button(text="+", height=15, width=13, command=button_add)
button_plus.grid(row=9, column=4, rowspan=3, padx=5, pady=5)
button_plus.place(relx=0.6, rely=0.675)

button_sub = Button(text="-", height=7, width=13, command=button_subtract)
button_sub.grid(row=8, column=3, padx=5, pady=5)
button_sub.place(relx=0.53, rely=0.530)

button_mult = Button(text="X", height=7, width=13, command=button_mult)
button_mult.grid(row=9, column=3, padx=5, pady=5)
button_mult.place(relx=0.53, rely=0.675)

button_div = Button(text="/", height=7, width=13, command=button_div)
button_div.grid(row=7, column=3, padx=5, pady=5)
button_div.place(relx=0.53, rely=0.385)

button_clear = Button(text="C", height=15, width=13, command=button_clear)
button_clear.grid(row=7, column=4, rowspan=2, columnspan=2, padx=5, pady=5)
button_clear.place(relx=0.6, rely=0.385)


window.mainloop()