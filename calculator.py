# Imports
import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

last_operation = 0
current_operation = 0 # 1 add 2 dif 3 mul 4 div 5 percentage

number_1 = 0
number_2 = 0

# Creating root
root = Tk() 
root.title("Calculator v.0.0.1")

e = Entry(root, width = 35, borderwidth = 5) #width, fg, bg, borderwidth = 20
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
e.insert(0, "0")

def button_click(number):
    current_string = e.get()
    e.delete(0, END)
    if current_string == '0':
        e.insert(0, str(number))
    else:
        e.insert(0, str(current_string) + str(number))

def set_operation(number):
    global number_1
    global current_operation
    number_1 = float(e.get())
    e.delete(0, END)
    if number == 5:
        result = number_1/100
        e.insert(0, result)
        current_operation = 0
    else:
        current_operation = number

def equal():
    global number_1
    global number_2
    global current_operation
    global last_operation
    result = 0
    if current_operation == 0:
        if last_operation == 1:
            result = float(e.get()) + number_2
        elif last_operation == 2:
            result = float(e.get()) - number_2
        elif last_operation == 3:
            result = float(e.get()) * number_2
        elif last_operation == 4:
            result = float(e.get()) / number_2
    else:
        number_2 = float(e.get())
        if current_operation == 1:
            result = number_1 + number_2
        elif current_operation == 2:
            result = number_1 - number_2
        elif current_operation == 3:
            result = number_1 * number_2
        elif current_operation == 4:
            result = number_1 / number_2
    e.delete(0, END)
    e.insert(0, result)
    if current_operation != 0:
        last_operation = current_operation
    current_operation = 0

def backspace():
    current_string = e.get()
    e.delete(0, END)
    e.insert(0, current_string[0:len(current_string)-1])
    if e.get() == '':
        e.insert(0, "0")

def clear():
    global number_1
    global current_operation
    e.delete(0, END)
    e.insert(0, "0")
    number_1 = 0
    current_operation = 0

button_x = 11
button_y = 3
button_1 = Button(root, text = '1', width = button_x, height = button_y, command = lambda: button_click(1))
button_2 = Button(root, text = '2', width = button_x, height = button_y, command = lambda: button_click(2))
button_3 = Button(root, text = '3', width = button_x, height = button_y, command = lambda: button_click(3))
button_4 = Button(root, text = '4', width = button_x, height = button_y, command = lambda: button_click(4))
button_5 = Button(root, text = '5', width = button_x, height = button_y, command = lambda: button_click(5))
button_6 = Button(root, text = '6', width = button_x, height = button_y, command = lambda: button_click(6))
button_7 = Button(root, text = '7', width = button_x, height = button_y, command = lambda: button_click(7))
button_8 = Button(root, text = '8', width = button_x, height = button_y, command = lambda: button_click(8))
button_9 = Button(root, text = '9', width = button_x, height = button_y, command = lambda: button_click(9))
button_0 = Button(root, text = '0', width = button_x, height = button_y, command = lambda: button_click(0))
button_dot = Button(root, text = '.', width = button_x, height = button_y, command = lambda: button_click('.'))
button_percentage = Button(root, text = '%', width = button_x, height = button_y, command = lambda: set_operation(5))
button_add = Button(root, text = '+', width = button_x, height = button_y, command = lambda: set_operation(1))
button_dif = Button(root, text = '-', width = button_x, height = button_y, command = lambda: set_operation(2))
button_mul = Button(root, text = '*', width = button_x, height = button_y, command = lambda: set_operation(3))
button_div = Button(root, text = '/', width = button_x, height = button_y, command = lambda: set_operation(4))
button_equal = Button(root, text = '=', width = 25, height = button_y, command = equal)
button_backspace = Button(root, text = '<--', width = 11, height = button_y, command = backspace)
button_clear = Button(root, text = 'clear', width = 11, height = button_y, command = clear)

button_1.grid(row=3, column = 0)
button_2.grid(row=3, column = 1)
button_3.grid(row=3, column = 2)

button_4.grid(row=2, column = 0)
button_5.grid(row=2, column = 1)
button_6.grid(row=2, column = 2)

button_7.grid(row=1, column = 0)
button_8.grid(row=1, column = 1)
button_9.grid(row=1, column = 2)

button_0.grid(row=4, column = 0)
button_dot.grid(row=4, column = 1)
button_percentage.grid(row=4, column = 2)

button_add.grid(row=1, column = 3)
button_dif.grid(row=2, column = 3)
button_mul.grid(row=3, column = 3)
button_div.grid(row=4, column = 3)

button_equal.grid(row=5, column = 0, columnspan = 2)
button_backspace.grid(row=5, column = 2)
button_clear.grid(row=5, column = 3)

# Functions
'''
def myClick():
    label = Label(root, text = e.get())
    label.pack()
'''
# Settings
root.bind('<F11>', lambda event: root.attributes('-fullscreen', not root.attributes("-fullscreen")))

# Creating things
#label_1 = Label(root, text = 'Hello world!')
#label_2 = Label(root, text = "My name is Pawel Perenc")

#button_1 = Button(root, text = 'Click me', padx = 50, pady = 20, command = myClick) # state = DISABLED, fg = "", bg = ""
#button_1.pack()

# Putting things on the screen
#label_1.grid(row = 0, column = 0)
#label_2.grid(row = 1, column = 0)


root.mainloop()

