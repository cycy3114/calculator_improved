"""
Calculator module with basic arithmetic operations and calculation history.
"""

from typing import List

class Calculator:
    """A simple calculator class to perform basic operations and keep history."""

    history: List[str] = []

    @staticmethod
    def add(x: float, y: float) -> float:
        """Return the sum of x and y and record the operation in history."""
        result = x + y
        Calculator.history.append(f"Added {x} + {y} = {result}")
        return result

    @staticmethod
    def subtract(x: float, y: float) -> float:
        """Return the difference of x and y and record the operation in history."""
        result = x - y
        Calculator.history.append(f"Subtracted {x} - {y} = {result}")
        return result

    @staticmethod
    def multiply(x: float, y: float) -> float:
        """Return the product of x and y and record the operation in history."""
        result = x * y
        Calculator.history.append(f"Multiplied {x} * {y} = {result}")
        return result

    @staticmethod
    def divide(x: float, y: float) -> float:
        """Return the quotient of x divided by y and record the operation in history.

        Raises:
            ZeroDivisionError: If y is zero.
        """
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = x / y
        Calculator.history.append(f"Divided {x} / {y} = {result}")
        return result

    @classmethod
    def get_history(cls) -> List[str]:
        """Return the history of calculations."""
        return cls.history
