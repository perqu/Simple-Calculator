import sys
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

import class_calculator

root = Tk() 
root.title("Calculator v.0.0.1")

mainContainer = Frame(root)
label = Label(mainContainer, text="")

display = Entry(root, width = 35, borderwidth = 5) #width, fg, bg, borderwidth = 20
display.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
display.insert(0, "0")

calc = class_calculator.Calculator(display)

def display_number():
    root.after(100,display_number)
    display.delete(0, END)
    display.insert(0, calc.display_operator())

display_number()

button_x = 11
button_y = 3
button_1 = Button(root, text = '1', width = button_x, height = button_y, command = lambda: calc.button_click(1))
button_2 = Button(root, text = '2', width = button_x, height = button_y, command = lambda: calc.button_click(2))
button_3 = Button(root, text = '3', width = button_x, height = button_y, command = lambda: calc.button_click(3))
button_4 = Button(root, text = '4', width = button_x, height = button_y, command = lambda: calc.button_click(4))
button_5 = Button(root, text = '5', width = button_x, height = button_y, command = lambda: calc.button_click(5))
button_6 = Button(root, text = '6', width = button_x, height = button_y, command = lambda: calc.button_click(6))
button_7 = Button(root, text = '7', width = button_x, height = button_y, command = lambda: calc.button_click(7))
button_8 = Button(root, text = '8', width = button_x, height = button_y, command = lambda: calc.button_click(8))
button_9 = Button(root, text = '9', width = button_x, height = button_y, command = lambda: calc.button_click(9))
button_0 = Button(root, text = '0', width = button_x, height = button_y, command = lambda: calc.button_click(0))
button_dot = Button(root, text = '.', width = button_x, height = button_y, command = lambda: calc.button_click('.'))
button_percentage = Button(root, text = '%', width = button_x, height = button_y, command = lambda: calc.set_operation(5))
button_add = Button(root, text = '+', width = button_x, height = button_y, command = lambda: calc.set_operation(1))
button_dif = Button(root, text = '-', width = button_x, height = button_y, command = lambda: calc.set_operation(2))
button_mul = Button(root, text = '*', width = button_x, height = button_y, command = lambda: calc.set_operation(3))
button_div = Button(root, text = '/', width = button_x, height = button_y, command = lambda: calc.set_operation(4))
button_equal = Button(root, text = '=', width = 25, height = button_y, command = calc.equal)
button_backspace = Button(root, text = '<--', width = 11, height = button_y, command = calc.backspace)
button_clear = Button(root, text = 'clear', width = 11, height = button_y, command = calc.clear)

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


# Settings
root.bind('<F11>', lambda event: root.attributes('-fullscreen', not root.attributes("-fullscreen")))

root.mainloop()
