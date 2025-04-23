import argparse
import sys

# Arithmetic operation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

# Main calculator function
def calculator():
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operation", type=str, help="Operation: add, sub, mul, div")

    args = parser.parse_args()

    operations = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide
    }

    if args.operation not in operations:
        print("❌ Unsupported operation. Use: add, sub, mul, div")
        sys.exit(1)
#try and except block to handle errors
    try:
        result = operations[args.operation](args.num1, args.num2)
        print(f"✅ Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    calculator()