class Calculator:
    history = []

    @staticmethod
    def add(a, b):
        result = a + b
        Calculator.history.append(f"Added {a} + {b} = {result}")
        return result

    @staticmethod
    def subtract(a, b):
        result = a - b
        Calculator.history.append(f"Subtracted {a} - {b} = {result}")
        return result

    @staticmethod
    def multiply(a, b):
        result = a * b
        Calculator.history.append(f"Multiplied {a} * {b} = {result}")
        return result

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        Calculator.history.append(f"Divided {a} / {b} = {result}")
        return result

    @staticmethod
    def get_history():
        return Calculator.history

