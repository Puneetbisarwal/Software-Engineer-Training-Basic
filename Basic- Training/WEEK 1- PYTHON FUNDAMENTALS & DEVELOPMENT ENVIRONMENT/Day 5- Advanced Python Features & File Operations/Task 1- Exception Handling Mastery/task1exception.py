# 3. Exception Hierarchy & Custom Exceptions

class InsufficientFundsError(Exception):
    """Raised when balance is too low for withdrawal"""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds.")
    return balance - amount


if __name__ == "__main__":
    # Create accounts
    savings = withdraw(1000, 200)
    checking = withdraw(500, 800)

    print(f"Savings after withdrawal: {savings}")
    print(f"Checking after withdrawal: {checking}")
    