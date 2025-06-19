from decimal import Decimal, InvalidOperation

class DivideCommand:
    def execute(self, a, b):
        try:
            return Decimal(a) / Decimal(b)
        except InvalidOperation:
            raise ValueError("Invalid numbers provided")
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
    
    def __str__(self):
        return "divide <num1> <num2> - Divides two numbers"
