import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    if "a" in metafunc.fixturenames and "b" in metafunc.fixturenames and "operation" in metafunc.fixturenames:
        num_records = metafunc.config.getoption("num_records")
        test_data = []
        
        for _ in range(num_records):
            a = fake.random_number(digits=2)
            b = fake.random_number(digits=2)
            operation = fake.random_element(elements=("add", "subtract", "multiply", "divide"))
            
            # Calculate expected result
            if operation == "add":
                expected = a + b
            elif operation == "subtract":
                expected = a - b
            elif operation == "multiply":
                expected = a * b
            elif operation == "divide":
                expected = a / b if b != 0 else None
            
            test_data.append((a, b, operation, expected))
        
        metafunc.parametrize("a,b,operation,expected", test_data)
