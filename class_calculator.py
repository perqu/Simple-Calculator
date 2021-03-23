import sys
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
        if not('.' in self.current_string and button == '.'):
            if self.current_string == '0':
                self.current_string = str(button)
            else:
                self.current_string += str(button)
            self.display_operator()

    def set_operation(self, operation):
        self.number2 = 'a'
        self.save_numbers('set')
        self.operation = operation
        self.current_string = ''
        if operation == '%':
            self.equal()
        self.display_operator()

    def equal(self):
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
        elif self.operation == '%':
            result = self.number1/100

        if not isinstance(self.number1, str) and not isinstance(self.number2, str):
            self.number1 = 'a'
            self.number2 = 'a'

        self.current_string = str(result)
        self.display_operator()

    def backspace(self):
        if len(self.current_string)>1:
            self.current_string = self.current_string[:-1]
        else:
            self.current_string = ''
        self.display_operator()

    def clear(self):
        self.number1 = 'a'
        self.number2 = 'a'
        self.current_string = ''
        self.operation = 0
        self.display_operator()

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
