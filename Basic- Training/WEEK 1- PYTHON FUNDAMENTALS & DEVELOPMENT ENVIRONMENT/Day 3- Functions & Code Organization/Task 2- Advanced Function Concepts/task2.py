"""
Task 2: Advanced Function Concepts
----------------------------------
This module demonstrates:
- *args and **kwargs
- Lambda functions
- Higher-order functions: map(), filter(), reduce()
- Recursive functions with base cases: factorial, fibonacci, binary search
"""

from functools import reduce


# ===== *args and **kwargs =====
def sum_all(*args):
    """
    Sum any number of positional numeric arguments.

    Parameters:
        *args (float): Numbers to sum.

    Returns:
        float: Sum of all arguments.
    """
    return sum(args)


def describe_person(**kwargs):
    """
    Describe a person using keyword arguments.

    Parameters:
        **kwargs: Arbitrary keyword arguments.

    Returns:
        str: Description of the person.
    """
    return ", ".join(f"{key}={value}" for key, value in kwargs.items())


# ===== Lambda functions =====
# Square numbers (short, inline function)
square = lambda x: x ** 2  # noqa: E731


# ===== Higher-order functions =====
def map_example(numbers):
    """
    Square numbers using map() and a lambda.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        list: Squared numbers.
    """
    return list(map(lambda x: x ** 2, numbers))


def filter_example(numbers):
    """
    Filter even numbers using filter() and a lambda.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        list: Even numbers only.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))


def reduce_example(numbers):
    """
    Multiply all numbers using reduce() and a lambda.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        int or float: Product of numbers.
    """
    return reduce(lambda x, y: x * y, numbers)


# ===== Recursive functions =====
def factorial_recursive(n):
    """
    Compute factorial recursively.

    Parameters:
        n (int): Non-negative integer.

    Returns:
        int: Factorial of n.
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_recursive(n):
    """
    Compute nth Fibonacci number recursively.

    Parameters:
        n (int): Position in Fibonacci sequence (0-based).

    Returns:
        int: Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def binary_search_recursive(arr, target, low=0, high=None):
    """
    Perform binary search recursively.

    Parameters:
        arr (list): Sorted list of elements.
        target: Element to find.
        low (int): Lower index bound.
        high (int): Upper index bound.

    Returns:
        int: Index of target, or -1 if not found.
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


# ===== Demonstration code =====
if __name__ == "__main__":
    # *args and **kwargs
    print(sum_all(1, 2, 3, 4, 5))
    print(describe_person(name="Akash", age=30, country="India"))

    # Lambda usage
    print(square(5))

    # Higher-order functions
    nums = [1, 2, 3, 4, 5]
    print(map_example(nums))
    print(filter_example(nums))
    print(reduce_example(nums))

    # Recursion
    print(factorial_recursive(5))
    print([fibonacci_recursive(i) for i in range(7)])
    print(binary_search_recursive([1, 3, 5, 7, 9], 7))
