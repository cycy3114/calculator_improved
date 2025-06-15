"""Pytest configuration for calculator tests with Faker data generation."""
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    """Add custom command line option for number of test records."""
    parser.addoption(
        "--num_records",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def pytest_generate_tests(metafunc):
    """Generate parameterized tests using Faker."""
    if {"a", "b", "operation", "expected"}.issubset(metafunc.fixturenames):
        num_records = metafunc.config.getoption("num_records")
        test_data = []

        for _ in range(num_records):
            a = fake.random_number(digits=2)
            b = fake.random_number(digits=2)
            operation = fake.random_element(("add", "subtract", "multiply", "divide"))

            expected = None
            if operation == "add":
                expected = a + b
            elif operation == "subtract":
                expected = a - b
            elif operation == "multiply":
                expected = a * b
            elif operation == "divide" and b != 0:
                expected = a / b

            test_data.append((a, b, operation, expected))

        metafunc.parametrize("a,b,operation,expected", test_data)
