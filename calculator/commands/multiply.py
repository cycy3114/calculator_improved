from decimal import Decimal, InvalidOperation

class MultiplyCommand:
    def execute(self, a, b):
        try:
            return Decimal(a) * Decimal(b)
        except InvalidOperation:
            raise ValueError("Invalid numbers provided")
    
    def __str__(self):
        return "multiply <num1> <num2> - Multiplies two numbers"
