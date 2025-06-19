from decimal import Decimal, InvalidOperation

class AddCommand:
    def execute(self, a, b):
        try:
            return Decimal(a) + Decimal(b)
        except InvalidOperation:
            raise ValueError("Invalid numbers provided")
    
    def __str__(self):
        return "add <num1> <num2> - Adds two numbers"
