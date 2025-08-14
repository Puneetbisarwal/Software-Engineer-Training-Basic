from abc import ABC, abstractmethod
from datetime import datetime


class Account(ABC):
    """Abstract base class for all bank accounts."""

    def __init__(self, account_number, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._log_transaction("Deposit", amount)

    @abstractmethod
    def withdraw(self, amount):
        """Withdraw money from account. Must be implemented by subclasses."""
        pass

    def _log_transaction(self, transaction_type, amount):
        """Log each transaction with date/time."""
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def get_statement(self):
        """Return account statement as a string."""
        statement_lines = [
            f"Statement for {self.owner} (Account: {self.account_number})",
            "-" * 50
        ]
        for t in self.transaction_history:
            statement_lines.append(
                f"{t['time']} | {t['type']:10} | {t['amount']:>8.2f} | Balance: {t['balance']:.2f}"
            )
        return "\n".join(statement_lines)


class SavingsAccount(Account):
    """Savings account with interest calculation."""

    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds in savings account.")
        self.balance -= amount
        self._log_transaction("Withdrawal", amount)

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction("Interest", interest)


class CheckingAccount(Account):
    """Checking account with overdraft protection."""

    def __init__(self, account_number, owner, balance=0, overdraft_limit=500):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount
        self._log_transaction("Withdrawal", amount)



if __name__ == "__main__":
    # Create accounts
    savings = SavingsAccount("S123", "Akshay", balance=1000, interest_rate=0.05)
    checking = CheckingAccount("C456", "Akash", balance=500, overdraft_limit=300)

    # Perform transactions
    savings.deposit(200)
    savings.withdraw(150)
    savings.add_interest()

    checking.deposit(100)
    checking.withdraw(700)  # Uses overdraft

    # Print statements
    print(savings.get_statement())
    print()
    print(checking.get_statement())
