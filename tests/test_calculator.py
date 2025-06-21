"""Test module for calculator operations with parameterized data."""
import pytest
from decimal import Decimal, InvalidOperation
from calculator.calculator import Calculator

@pytest.mark.parametrize("first_num,second_num,operation,expected", [
    (10, 5, "add", 15),
    (10, 5, "subtract", 5),
    (10, 5, "multiply", 50),
    (10, 5, "divide", 2),
    (0.1, 0.2, "add", 0.3),  # Test floating point precision

    (10, 0, "divide", "Error: Cannot divide by zero"),
    (10, "first_num", "add", "Error: Invalid numbers provided"),
    ("x", 5, "multiply", "Error: Invalid numbers provided"),
    (10, 5, "power", "Error: Unknown operation"),  # Test invalid operation

    # Edge cases
    (999999999, 1, "add", 1000000000),  # Large numbers (fixed expected value)
    (0, 0, "add", 0),  # Zero cases
])
def test_calculator_operations(first_num, second_num, operation, expected):
    """Test calculator operations with dynamically generated data.

    Args:
        first_num: First test number
        second_num: Second test number
        operation: Math operation to test
        expected: Expected result
    """
    calc = Calculator()
    
    if isinstance(expected, str) and expected.startswith("Error:"):
        # Test for expected error cases
        with pytest.raises(ValueError, match=expected[7:]):
            calc.calculate(operation, first_num, second_num)
    else:
        # Test normal operations
        result = calc.calculate(operation, first_num, second_num)
        # Compare using Decimal for precise floating point assertions
        assert Decimal(str(result)).quantize(Decimal('1.00000000')) == Decimal(str(expected)).quantize(Decimal('1.00000000'))
