from faker import Faker
from calculator.calculation import Calculator

fake = Faker()

def test_fake_addition():
    a = fake.random_int(min=1, max=100)
    b = fake.random_int(min=1, max=100)
    result = Calculator.add(a, b)
    assert result == a + b
def test_generated(random_operations):
    if operation == "add":
        assert Calculator.add(a, b) == expected
    elif operation == "subtract":
        assert Calculator.subtract(a, b) == expected
    elif operation == "multiply":
        assert Calculator.multiply(a, b) == expected
    elif operation == "divide":
        assert Calculator.divide(a, b) == pytest.approx(expected)
def test_generated(a, b, operation, expected):
    from calculator.calculation import Calculator
    if operation == "add":
        assert Calculator.add(a, b) == expected
    elif operation == "subtract":
        assert Calculator.subtract(a, b) == expected
    elif operation == "multiply":
        assert Calculator.multiply(a, b) == expected
    elif operation == "divide":
        assert Calculator.divide(a, b) == expected
