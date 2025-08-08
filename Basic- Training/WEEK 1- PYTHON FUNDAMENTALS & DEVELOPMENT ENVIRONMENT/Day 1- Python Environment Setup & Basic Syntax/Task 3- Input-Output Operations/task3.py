# Task 3: Input/Output Operations


# Program to ask for name, age, and calculate birth year

# Ask for name
name = input("Enter your name: ")

# Ask for age with validation
while True:
    age_input = input("Enter your age: ")
    if age_input.isdigit():  # Checks if input is all digits
        age = int(age_input)  # Convert to integer
        break
    else:
        print("Invalid age. Please enter a number.")

# Calculate birth year
from datetime import datetime
current_year = datetime.now().year
birth_year = current_year - age

# Print result
print(f"\nHello {name}!")
print(f"You are {age} years old.")
print(f"You were born in {birth_year}.")
