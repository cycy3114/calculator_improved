"""Test module for calculator operations with parameterized data."""
from calculator.calculator import Calculator

def test_calculator_operations(first_num, second_num, operation, expected):
    """Test calculator operations with dynamically generated data.

    Args:
        first_num: First test number 
        second_num: Second test number
        operation: Math operation to test
        expected: Expected result
    """
    calc = Calculator()
    if operation == "add":
        assert calc.add(first_num, second_num) == expected
    elif operation == "subtract":
        assert calc.subtract(first_num, second_num) == expected
    elif operation == "multiply":
        assert calc.multiply(first_num, second_num) == expected
    elif operation == "divide" and second_num != 0:
        assert calc.divide(first_num, second_num) == expected
