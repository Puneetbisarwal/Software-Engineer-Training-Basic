"""
Module: basics
Task 1: Function Fundamentals
"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Return sum of two numbers."""
    return f"Sum is: {a + b}"

def multiply_numbers(a, b=1):
    """Return product of two numbers (default b=1)."""
    return f"Product is: {a * b}"

# Variable scope example
x_global = 50
def scope_demo():
    """Demonstrate local vs global scope."""
    global x_global
    x_global += 5
    return x_global


if __name__ == "__main__":
    print(greet("Abhishek"))