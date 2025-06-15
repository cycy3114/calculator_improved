from calculator import Calculator

def test_calculator_operations(a, b, operation, expected):
    calc = Calculator()
    if operation == "add":
        assert calc.add(a, b) == expected
    elif operation == "subtract":
        assert calc.subtract(a, b) == expected
    elif operation == "multiply":
        assert calc.multiply(a, b) == expected
    elif operation == "divide" and b != 0:
        assert calc.divide(a, b) == expected
