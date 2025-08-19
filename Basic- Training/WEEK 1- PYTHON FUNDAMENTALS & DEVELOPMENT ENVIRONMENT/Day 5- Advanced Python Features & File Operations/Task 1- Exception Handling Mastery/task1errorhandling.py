# 4. Graceful Error Handling in User Apps

class InsufficientFundsError(Exception):
    """Raised when balance is too low for withdrawal"""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds.")
    return balance - amount

try:
    amount = float(input("Enter withdrawal amount: "))
    balance = withdraw(500, amount)
    print(f"Withdrawal successful! New balance: {balance}")
except ValueError:
    print("Invalid input. Please enter a number.")
except InsufficientFundsError as e:
    print(f"Error: {e}")
finally:
    print("Transaction attempt completed.")
    