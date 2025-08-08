"""
Command-Line Calculator
=======================

A simple command-line calculator supporting:
+  (Addition)
-  (Subtraction)
*  (Multiplication)
/  (Division)
%  (Modulo)
** (Exponentiation)

Features:
- Input validation for numbers and operators
- Error handling for division/modulo by zero
- Calculation history
- Organized using functions for clarity and reuse

Author: Puneet
Date: 2025-08-08
"""

# -------- Global History List --------
history = []


def get_number(prompt):
    """
    Prompt the user for a number with validation.

    Args:
        prompt (str): Message displayed to the user.

    Returns:
        float: The numeric value entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def get_operator():
    """
    Prompt the user for a valid mathematical operator.

    Returns:
        str: The operator entered by the user.
    """
    valid_ops = ['+', '-', '*', '/', '%', '**']
    while True:
        op = input("Enter operator (+, -, *, /, %, **): ").strip()
        if op in valid_ops:
            return op
        print(f"❌ Invalid operator. Choose from {', '.join(valid_ops)}.")


def calculate(a, b, op):
    """
    Perform a calculation based on the operator provided.

    Args:
        a (float): First operand.
        b (float): Second operand.
        op (str): Mathematical operator.

    Returns:
        float or None: The calculation result, or None on error.
    """
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
        print(f"❌ {e}")
        return None


def add_to_history(a, b, op, result):
    """
    Add a calculation record to the history.

    Args:
        a (float): First operand.
        b (float): Second operand.
        op (str): Operator used.
        result (float): Result of calculation.
    """
    if result is not None:
        history.append(f"{a} {op} {b} = {result}")


def show_history():
    """
    Display all previous calculations.
    """
    if history:
        print("\n📜 Calculation History:")
        for i, record in enumerate(history, 1):
            print(f"{i}. {record}")
    else:
        print("\nℹ No history yet.")


def run_calculator():
    """
    Main calculator loop.
    Handles user input, performs calculations, and manages history.
    """
    print("🧮 Welcome to the Python Calculator!")
    while True:
        a = get_number("Enter first number: ")
        op = get_operator()
        b = get_number("Enter second number: ")

        result = calculate(a, b, op)
        if result is not None:
            print(f"✅ Result: {result}")
            add_to_history(a, b, op, result)

        if input("\nDo you want to see history? (y/n): ").lower() == 'y':
            show_history()

        if input("\nDo you want to perform another calculation? (y/n): ").lower() != 'y':
            print("👋 Goodbye!")
            break


# Run program if script is executed directly
if __name__ == "__main__":
    run_calculator()


# ----------- Test Cases -----------
def test_calculator():
    """
    Basic unit tests for calculator functions.
    """
    assert calculate(5, 3, '+') == 8
    assert calculate(5, 3, '-') == 2
    assert calculate(5, 3, '*') == 15
    assert calculate(6, 3, '/') == 2
    assert calculate(6, 3, '%') == 0
    assert calculate(2, 3, '**') == 8
    assert calculate(5, 0, '/') is None  # Division by zero
    assert calculate(5, 0, '%') is None  # Modulo by zero
    print("✅ All tests passed!")
