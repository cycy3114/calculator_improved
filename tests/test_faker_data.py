from faker import Faker
from calculator.calculations import perform_calculation

fake = Faker()

def test_faker_generated_data():
    for _ in range(5):  # Generate 5 test cases
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        result = perform_calculation(a, b, 'add')
        expected = f"The result of {a} add {b} is equal to {a + b}"
        assert result == expected
