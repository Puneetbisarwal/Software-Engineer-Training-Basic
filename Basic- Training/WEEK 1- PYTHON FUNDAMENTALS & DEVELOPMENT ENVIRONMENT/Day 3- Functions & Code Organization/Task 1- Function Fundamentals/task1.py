"""
Task 1: Function Fundamentals
-----------------------------
This module contains 10 utility functions demonstrating:
- Function definition using `def`
- Positional, keyword, and default parameters
- Return statements with single and multiple values
- Variable scope: local, global, and nonlocal
"""

# ===== Example of a global variable =====
GLOBAL_COUNTER = 0


def greet_user(name, greeting="Hello"):
    """
    Greet a user with a given message.

    Parameters:
        name (str): The name of the user.
        greeting (str, optional): The greeting message. Default is "Hello".

    Returns:
        str: A formatted greeting message.
    """
    return f"{greeting}, {name}!"


def add_numbers(a, b):
    """
    Add two numbers.

    Parameters:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


def divide_numbers(numerator, denominator):
    """
    Divide two numbers safely.

    Parameters:
        numerator (float): The numerator.
        denominator (float): The denominator.

    Returns:
        float or None: Result of division or None if denominator is zero.
    """
    if denominator == 0:
        return None
    return numerator / denominator


def get_min_max(numbers):
    """
    Get the minimum and maximum from a list of numbers.

    Parameters:
        numbers (list): A list of numeric values.

    Returns:
        tuple: (min_value, max_value)
    """
    return min(numbers), max(numbers)


def factorial(n):
    """
    Calculate factorial of a number recursively.

    Parameters:
        n (int): A non-negative integer.

    Returns:
        int: Factorial of n.
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def increment_global():
    """
    Increment the global counter variable.

    Returns:
        int: Updated global counter.
    """
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    return GLOBAL_COUNTER


def counter_closure():
    """
    Demonstrate nonlocal variable scope using a closure.

    Returns:
        function: A function that increments a nonlocal counter.
    """
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    return inner


def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
        number (int): The number to check.

    Returns:
        bool: True if number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def reverse_string(text):
    """
    Reverse a given string.

    Parameters:
        text (str): String to reverse.

    Returns:
        str: Reversed string.
    """
    return text[::-1]


def calculate_area(shape, **kwargs):
    """
    Calculate area of different shapes using keyword arguments.

    Parameters:
        shape (str): Type of shape ('circle', 'rectangle', 'triangle').
        kwargs: Parameters for shape dimensions.

    Returns:
        float: Area of the shape, or None if shape is invalid.
    """
    import math

    if shape.lower() == "circle":
        radius = kwargs.get("radius", 0)
        return math.pi * radius ** 2
    elif shape.lower() == "rectangle":
        return kwargs.get("width", 0) * kwargs.get("height", 0)
    elif shape.lower() == "triangle":
        return 0.5 * kwargs.get("base", 0) * kwargs.get("height", 0)
    return None


# ===== Demonstration code =====
if __name__ == "__main__":
    print(greet_user("Akash"))
    print(add_numbers(5, 7))
    print(divide_numbers(10, 2))
    print(get_min_max([1, 3, 5, 0, -1]))
    print(factorial(5))
    print(increment_global())
    print(increment_global())
    counter = counter_closure()
    print(counter())
    print(counter())
    print(is_prime(29))
    print(reverse_string("Python"))
    print(calculate_area("circle", radius=5))
    print(calculate_area("rectangle", width=4, height=6))
