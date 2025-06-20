"""Test module for calculator operations with parameterized data."""
import pytest
from calculator.calculator import Calculator

@pytest.mark.parametrize("first_num,second_num,operation,expected", [
    (10, 5, "add", 15),
    (10, 5, "subtract", 5),
    (10, 5, "multiply", 50),
    (10, 5, "divide", 2),
    (10, 0, "divide", "Error: Cannot divide by zero"),
    (10, "a", "add", "Error: Invalid numbers provided")
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
        assert round(result, 8) == round(expected, 8)
