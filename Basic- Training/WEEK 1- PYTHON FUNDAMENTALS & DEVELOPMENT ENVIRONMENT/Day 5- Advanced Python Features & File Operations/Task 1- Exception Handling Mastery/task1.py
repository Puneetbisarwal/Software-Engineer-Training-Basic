# 1. Master try/except/else/finally

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result is {result}")
finally:
    print("Program finished (cleanup done).")

# 2. Learn Specific Exception Types    

print("\nLearn Specific Exception Types")
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError:
    print("Index out of range!")
    
    





