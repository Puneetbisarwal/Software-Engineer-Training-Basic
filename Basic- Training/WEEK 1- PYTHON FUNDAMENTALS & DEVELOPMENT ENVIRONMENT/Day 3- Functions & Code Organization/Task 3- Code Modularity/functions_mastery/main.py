"""
Main entry point for Functions Mastery Project
"""

from basics import greet, add_numbers, scope_demo, multiply_numbers
from advanced import (
    sum_all, describe_person, square,
    map_example, filter_example, reduce_example,
    factorial_recursive, fibonacci_recursive, binary_search_recursive
)

if __name__ == "__main__":
    # Task 1 demos
    print(greet("Akash"))
    print(add_numbers(5, 7))
    print(scope_demo())
    print(multiply_numbers(5, 10))
    print("----------")

    # Task 2 demos
    print(sum_all(1, 2, 3, 4))
    print(describe_person(name="Chandan", age=25))
    print(square(6))
    nums = [1, 2, 3, 4, 5]
    print(map_example(nums))
    print(filter_example(nums))
    print(reduce_example(nums))
    print(factorial_recursive(5))
    print([fibonacci_recursive(i) for i in range(6)])
    print(binary_search_recursive([1, 3, 5, 7, 9], 7))
