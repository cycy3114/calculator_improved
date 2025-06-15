import sys
from calculator import Calculator

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Operations: add, subtract, multiply, divide")
        return
    
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
    except ValueError:
        print(f"Invalid number input: {sys.argv[1]} or {sys.argv[2]} is not a valid number.")
        return
    
    operation = sys.argv[3].lower()
    calc = Calculator()
    
    try:
        if operation == "add":
            result = calc.add(a, b)
        elif operation == "subtract":
            result = calc.subtract(a, b)
        elif operation == "multiply":
            result = calc.multiply(a, b)
        elif operation == "divide":
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = calc.divide(a, b)
        else:
            print(f"Unknown operation: {operation}")
            return
        
        print(f"The result of {a} {operation} {b} is equal to {result}")
    except ZeroDivisionError as e:
        print(f"An error occurred: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
