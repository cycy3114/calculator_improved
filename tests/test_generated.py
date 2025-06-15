import pytest
from faker import Faker
from calculator.calculations import add, subtract, multiply, divide

fake = Faker()

def pytest_generate_tests(metafunc):
    if {"a", "b", "operation", "expected"}.issubset(metafunc.fixturenames):
        operations = ['add', 'subtract', 'multiply', 'divide']
        test_cases = []
        for _ in range(metafunc.config.getoption("--num_records")):
            a = fake.random_int(min=1, max=100)
            b = fake.random_int(min=1, max=100)
            op = fake.random_element(operations)
            if op == "add":
                expected = a + b
            elif op == "subtract":
                expected = a - b
            elif op == "multiply":
                expected = a * b
            elif op == "divide":
                expected = a / b if b != 0 else None
            test_cases.append((a, b, op, expected))
        metafunc.parametrize("a,b,operation,expected", test_cases)

def test_generated_data(a, b, operation, expected):
    if operation == "divide" and b == 0:
        with pytest.raises(ZeroDivisionError):
            divide(a, b)
    else:
        if operation == "add":
            assert add(a, b) == expected
        elif operation == "subtract":
            assert subtract(a, b) == expected
        elif operation == "multiply":
            assert multiply(a, b) == expected
        elif operation == "divide":
            assert divide(a, b) == expected

