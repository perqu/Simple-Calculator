import sys
import tkinter.font as font
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

'''
import win32gui, win32con
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
'''

def display_number():
    root.after(100,display_number)
    display.delete(0, END)
    display.insert(0, calc.display_operator())

import class_calculator

root = Tk() 
root.title("Calculator v.0.0.1")

#font
myFont = font.Font(family='Helvetica', size=30, weight='bold')

display = Entry(root, width = 27, font = myFont, borderwidth = 5) #width, fg, bg, borderwidth = 20

calc = class_calculator.Calculator()

# size of buttons
button_x = 5
button_y = 2
# Button click
button_1 = Button(root, text = '1', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(1))
button_2 = Button(root, text = '2', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(2))
button_3 = Button(root, text = '3', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(3))
button_4 = Button(root, text = '4', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(4))
button_5 = Button(root, text = '5', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(5))
button_6 = Button(root, text = '6', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(6))
button_7 = Button(root, text = '7', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(7))
button_8 = Button(root, text = '8', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(8))
button_9 = Button(root, text = '9', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(9))
button_0 = Button(root, text = '0', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_click(0))
# Button dot
button_dot = Button(root, text = '.', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_dot('.'))
# Button operation
button_percentage = Button(root, text = '%', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('%'))
button_add = Button(root, text = '+', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('+'))
button_dif = Button(root, text = '-', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('-'))
button_mul = Button(root, text = '*', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('*'))
button_div = Button(root, text = '/', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('/'))
button_mod = Button(root, text = 'mod', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('mod'))
button_x2 = Button(root, text = 'x**2', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('** 2'))
button_xy = Button(root, text = 'x**y', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('**'))
button_2p = Button(root, text = '2 _\n√x', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('2√'))
button_yp = Button(root, text = 'y _\n√x', font = myFont, width = button_x, height = button_y, command = lambda: calc.button_operation('√'))
# Button equal
button_equal = Button(root, text = '=', font = myFont, width = button_x, height = button_y, command = calc.button_equal)
# Button change
button_change = Button(root, text = '+/-', font = myFont, width = button_x, height = button_y, command = calc.button_change)
# Button backspace
button_backspace = Button(root, text = '<--', font = myFont, width = button_x, height = button_y, command = calc.button_backspace)
# Button clear
button_clear = Button(root, text = 'clear', font = myFont, width = button_x, height = button_y, command = calc.button_clear)

# Display - row 0
display.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady = 10)

# Column 0
button_7.grid(row=1, column = 0)
button_4.grid(row=2, column = 0)
button_1.grid(row=3, column = 0)
button_0.grid(row=4, column = 0)
button_equal.grid(row=5, column = 0)

# Column 1
button_8.grid(row=1, column = 1)
button_5.grid(row=2, column = 1)
button_2.grid(row=3, column = 1)
button_dot.grid(row=4, column = 1)
button_backspace.grid(row=5, column = 1)

# Column 2
button_9.grid(row=1, column = 2)
button_6.grid(row=2, column = 2)
button_3.grid(row=3, column = 2)
button_change.grid(row=4, column = 2)
button_clear.grid(row=5, column = 2)

# Column 3
button_add.grid(row=1, column = 3)
button_dif.grid(row=2, column = 3)
button_mul.grid(row=3, column = 3)
button_div.grid(row=4, column = 3)
button_percentage.grid(row=5, column = 3)

# Column 4
button_mod.grid(row=1, column = 4)
button_x2.grid(row=2, column = 4)
button_xy.grid(row=3, column = 4)
button_2p.grid(row=4, column = 4)
button_yp.grid(row=5, column = 4)

# Keybinds
root.bind('<F11>', lambda event: root.attributes('-fullscreen', not root.attributes("-fullscreen")))

# Looping function
display_number()

# Main loop
root.mainloop()