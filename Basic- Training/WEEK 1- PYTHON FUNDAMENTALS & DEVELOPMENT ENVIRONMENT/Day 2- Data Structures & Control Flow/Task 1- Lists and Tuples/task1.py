# Start with a list of fruits
fruits = ["apple", "banana", "cherry"]

# 1a. Append "orange" to the list
fruits.append("orange")
# 1b. Extend the list with ["grape", "mango"]
fruits.extend(["grapes", "mangos"])
print(fruits)

# Insert "kiwi" at index 1
fruits.insert(1, "kiwi")
print(fruits)

# Remove "banana" by value
fruits.remove("banana")
last_fruit = fruits.pop()
print("Popped fruit:", last_fruit)
print(fruits)

# Print the first fruit
print("First fruit:", fruits[0])
# Print the last two fruits using slicing
print("Last two fruits:", fruits[-2:])

# Create a tuple called colors with 3 color names
colors = ("red", "green", "blue")
print(colors)
# Try to change one element of the tuple and see what happens
# colors[0] = "yellow"   # This will raise a TypeError because tuples are immutable
print(colors)

# Create a list of squares from 1 to 10 using list comprehension
squares = [x**2 for x in range(1, 11)]
print(squares)


# Given a list of temperatures in Celsius, convert them to Fahrenheit
# Formula: F = C * 9/5 + 32
celsius = [0, 20, 37, 100]
fahrenheit = [temp * 9/5 + 32 for temp in celsius]
print(fahrenheit)
