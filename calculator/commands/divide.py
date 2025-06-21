from decimal import Decimal, InvalidOperation

class DivideCommand:
    """Command class for division operation with proper error handling."""

    def execute(self, a, b):
        """
        Execute division operation with validation.

        Args:
            a: First number (dividend)
            b: Second number (divisor)

        Returns:
            float: Result of a divided by b

        Raises:
            ValueError: If inputs are invalid or division by zero occurs
        """
        try:
            # Convert inputs to Decimal via string to maintain precision
            a_dec = Decimal(str(a))
            b_dec = Decimal(str(b))

            # Explicit check for zero division
            if b_dec == 0:
                raise ZeroDivisionError

            # Perform division and convert to float for consistency
            return float(a_dec / b_dec)

        except InvalidOperation:
            raise ValueError("Invalid numbers provided")
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")

    def __str__(self):
        """Return help text for the divide command."""
        return "divide <num1> <num2> - Divides two numbers (divisor cannot be zero)"

