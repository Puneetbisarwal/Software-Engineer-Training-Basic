# Task 4: Command-Line Calculator Project


# Simple Calculator with History

# Store history in a list
history = []

def get_number(prompt):
    """Prompt user for a number with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operator():
    """Prompt user for a valid operator."""
    valid_ops = ['+', '-', '*', '/', '%', '**']
    while True:
        op = input("Enter operator (+, -, *, /, %, **): ").strip()
        if op in valid_ops:
            return op
        else:
            print(f"Invalid operator. Choose from {', '.join(valid_ops)}.")

def calculate(a, b, op):
    """Perform calculation based on operator."""
    try:
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return a / b
        elif op == '%':
            if b == 0:
                raise ZeroDivisionError("Modulo by zero is not allowed.")
            return a % b
        elif op == '**':
            return a ** b
    except ZeroDivisionError as e:
        print(e)
        return None

def add_to_history(a, b, op, result):
    """Add a calculation record to history."""
    if result is not None:
        history.append(f"{a} {op} {b} = {result}")

def show_history():
    """Display calculation history."""
    if history:
        print("\nCalculation History:")
        for i, record in enumerate(history, 1):
            print(f"{i}. {record}")
    else:
        print("\nNo history yet.")

def run_calculator():
    """Main calculator loop."""
    print("Welcome to the Python Calculator!")
    while True:
        a = get_number("Enter first number: ")
        op = get_operator()
        b = get_number("Enter second number: ")
        
        result = calculate(a, b, op)
        if result is not None:
            print(f"Result: {result}")
            add_to_history(a, b, op, result)
        
        choice = input("\nDo you want to see history? (y/n): ").lower()
        if choice == 'y':
            show_history()
        
        again = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

# ----------- Run the calculator -----------
if __name__ == "__main__":
    run_calculator()


# ----------- Basic Test Cases -----------
def test_calculator():
    assert calculate(5, 3, '+') == 8
    assert calculate(5, 3, '-') == 2
    assert calculate(5, 3, '*') == 15
    assert calculate(6, 3, '/') == 2
    assert calculate(6, 3, '%') == 0
    assert calculate(2, 3, '**') == 8
    assert calculate(5, 0, '/') is None  # Division by zero
    assert calculate(5, 0, '%') is None  # Modulo by zero
    print("All tests passed!")

# Uncomment to run tests
# test_calculator()
