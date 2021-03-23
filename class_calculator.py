import sys
import math
if sys.version_info[0] == 2:  # Just checking your Python version to import Tkinter properly.
    from Tkinter import *
else:
    from tkinter import *

class Calculator():

    number1 = 'a'
    number2 = 'a'
    memory = 0

    # 1 add 2 dif 3 mul 4 div 5 percentage
    operation = 0 

    current_string = ''

    def __init__(self):
        pass

    def button_click(self, button):
            if self.current_string == '0':
                self.current_string = str(button)
            else:
                self.current_string += str(button)

    def button_dot(self, button):
        if not('.' in self.current_string and button == '.'):
            self.current_string += str(button)

    def button_operation(self, operation):
        self.number2 = 'a'
        self.save_numbers('set')
        self.operation = operation
        self.current_string = ''
        if operation == '%' or operation == '**2' or operation == '2√':
            self.button_equal()

    def button_equal(self):
        self.save_numbers('equal')
        if isinstance(self.number1, str) or isinstance(self.number2, str):
            self.number2 = self.memory
        result = 0
        if self.operation == '+':
            result = self.number1 + self.number2
        elif self.operation == '-':
            result = self.number1 - self.number2
        elif self.operation == '*':
            result = self.number1 * self.number2
        elif self.operation == '/':
            result = self.number1 / self.number2
        elif self.operation == 'mod':
            result = self.number1 % self.number2
        elif self.operation == '**':
            result = self.number1 ** self.number2
        elif self.operation == '2√':
            result = self.number1 ** (1/2)
        elif self.operation == '√':
            result = self.number1 ** (1/self.number2)
        elif self.operation == '**2':
            result = self.number1 ** 2
        elif self.operation == '%':
            result = self.number1/100

        if not isinstance(self.number1, str) and not isinstance(self.number2, str):
            self.number1 = 'a'
            self.number2 = 'a'

        self.current_string = str(result)

    def button_backspace(self):
        if len(self.current_string)>1:
            self.current_string = self.current_string[:-1]
        else:
            self.current_string = ''

    def button_clear(self):
        self.number1 = 'a'
        self.number2 = 'a'
        self.current_string = ''
        self.operation = 0

    def button_change(self):
        self.current_string = str(-float(self.current_string))

    def save_numbers(self, method):
        try:
            if self.number1 == 'a':
                self.number1 = float(self.current_string)
            elif self.number2 == 'a':
                self.number2 = float(self.current_string)
                self.memory = self.number2
            elif not isinstance(self.number1, str) and not isinstance(self.number2, str) and method == 'equal':
                self.number1 = float(self.current_string)
        except:
            pass

    def display_operator(self):
        display_string = ''
        if self.number1 != 'a':
            display_string += str(self.number1) + "  "
            if self.operation != 0:
                display_string += str(self.operation) + "  "
        display_string += self.current_string
        return display_string
