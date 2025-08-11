# Program: Ticket Pricing System
age = 25
is_student = True

if age < 12:
    price = 5
elif age < 18 or is_student:
    price = 8
elif age >= 60:
    price = 6
else:
    price = 10

print(f"Ticket Price: ${price}")



# Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Loop over a string
for char in "Hi!":
    print("Character:", char)

# Loop over a range
for i in range(1, 6):
    print("Number:", i)


# Program: Guess the Number
secret = 7
guess = None

while True:
    guess = int(input("Guess a number (1-10): "))
    if guess < 1 or guess > 10:
        print("Out of range! Try again.")
        continue
    if guess == secret:
        print("🎉 Correct!")
        break
    else:
        print("Wrong guess, try again.")



# Program: Multiplication Table (1 to 3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("-" * 10)



# Program: Find First Even Number in List (optimized)
numbers = [1, 3, 5, 8, 10, 12]

for num in numbers:
    if num % 2 == 0:
        print("First even number found:", num)
        break  # Stop loop early once found
