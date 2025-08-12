"""
Module: advanced
Task 2: Advanced Function Concepts
"""

from functools import reduce

def sum_all(*args):
    return sum(args)

def describe_person(**kwargs):
    return ", ".join(f"{k}={v}" for k, v in kwargs.items())

square = lambda x: x ** 2  # noqa: E731

def map_example(numbers):
    return list(map(lambda x: x ** 2, numbers))

def filter_example(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

def reduce_example(numbers):
    return reduce(lambda x, y: x * y, numbers)

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def binary_search_recursive(arr, target, low=0, high=None):
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
