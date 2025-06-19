import sys
from calculator.calculator import Calculator

def main():
    calc = Calculator()

    # If no arguments, start REPL
    if len(sys.argv) == 1:
        calc.start_repl()
        return

    # Handle command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        print("Operations: add, subtract, multiply, divide")
        return

    try:
        a = sys.argv[1]
        b = sys.argv[2]
        operation = sys.argv[3].lower()

        result = calc.calculate(operation, a, b)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
