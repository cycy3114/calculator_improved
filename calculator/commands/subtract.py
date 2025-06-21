from decimal import Decimal, InvalidOperation

class SubtractCommand:
    def execute(self, a, b):
        try:
            return Decimal(a) - Decimal(b)
        except InvalidOperation:
            raise ValueError("Invalid numbers provided")

    def __str__(self):
        return "subtract <num1> <num2> - Subtracts two numbers"
