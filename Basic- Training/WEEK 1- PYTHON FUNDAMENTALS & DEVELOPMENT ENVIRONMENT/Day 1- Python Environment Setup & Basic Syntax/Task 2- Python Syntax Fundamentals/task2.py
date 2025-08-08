# Task 2: Python Syntax Fundamentals

# Variables & Naming

# Create a variable to store your name
name = "Puneet"

# Print the name
print(name)

# Store your age in a variable
age = 25

# Print the sentence
print(f"I am {age} years old.")
print("I am {} years old.".format(age))
print("I am %d years old." % age)

# Define a constant for PI (by convention, constants are in ALL_CAPS)
PI = 3.14159

# Print the value of PI
print(PI)


# Badly named variable
x1 = 85

# Rename it to a descriptive name
user_score = x1

# Print the score
print(user_score)


# Data Types

# Create variables of different types
age = 25               # int
height = 5.9           # float
name = "Puneet"        # str
is_student = True      # bool

# Print the variables and their types
print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))


# Start with an integer
age = 25
print(age, type(age))  # int

# Change the value to a string
age = "25"
print(age, type(age))  # str

# Assign the same value to three variables in one line
a = b = c = 100

# Print them
print(a, b, c)

# Initial values
x = 5
y = 10

# Swap without temp variable
x, y = y, x

# Print results
print("x =", x)
print("y =", y)


# String Formatting

balance = 500
print(f"Your balance is ${balance}")

name = "Akash"
score = 95

print("{} scored {} marks in Maths.".format(name, score))
print("{0} scored {1} points".format(name, score))       # positional
print("{player} scored {points} points".format(player=name, points=score))  # named

temperature = 22.51
print("Temperature is %.1f°C" % temperature)
print("Temperature is %s°C" % temperature)

price = 45.6789
print(f"Price: {price:.2f}")
print("Price: %.2f" % price)

# Dynamic Typing


# Assign an integer
value = 100
print(value)

# Assign a string to the same variable
value = "One Hundred"
print(value)

def print_type(value):
    print(f"The type of {value} is {type(value)}")

# Test the function
print_type(10)         # int
print_type(3.14)       # float
print_type("Hello")    # str
print_type(True)       # bool

# Assign None to a variable
data = None

# Print its type
print(data, type(data))


# Mixed Challenges


part1 = "Python"
part2 = "is"
part3 = "fun"

# Concatenate with spaces
sentence = part1 + " " + part2 + " " + part3

print(sentence)
print(f"{part1} {part2} {part3}")
print("{0} {1} {2}".format(part1, part2, part3))
print("{first} {second} {third}".format(first=part1, second=part2, third=part3))

text = "Hello "
print(text * 5)

print(f"5 + 3 = {5 + 3}")
print("5 + 3 = {}".format(5 + 3))
print("5 + 3 = %d" % (5 + 3))

# Get user input
text = input("Enter something: ")

# Print in uppercase
print(text.upper())

name = "Puneet"
age = 25
city = "New Delhi"

info = f"""
Name: {name}
Age: {age}
City: {city}
"""

print(info)
