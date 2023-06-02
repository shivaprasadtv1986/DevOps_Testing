"""
Python calculator program.
"""

class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b


    def substraction(self):
        return self.a - self.b


    def multiplication(self):
        return self.a * self.b


    def division(self):
        return self.a / self.b

"""
a = 10
b = 5
cal = Calculator(a,b)
print(cal.addition())
print(cal.substraction())
print(cal.multiplication())
print(cal.division())
"""

