def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def perform_calculation(a, b, operation):
    if operation == "add":
        return f"The result of {a} add {b} is equal to {add(a, b)}"
    elif operation == "subtract":
        return f"The result of {a} subtract {b} is equal to {subtract(a, b)}"
    elif operation == "multiply":
        return f"The result of {a} multiply {b} is equal to {multiply(a, b)}"
    elif operation == "divide":
        try:
            return f"The result of {a} divide {b} is equal to {divide(a, b)}"
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return f"Unknown operation: {operation}"

def perform_calculation(a, b, operation: str):
    if operation == "add":
        return str(add(a, b))
    elif operation == "subtract":
        return str(subtract(a, b))
    elif operation == "multiply":
        return str(multiply(a, b))
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return str(divide(a, b))
    else:
        return "Invalid operation"
