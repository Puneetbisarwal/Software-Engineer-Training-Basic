from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict


class Account(ABC):
    """
    Abstract base class representing a generic bank account.

    Attributes:
        account_number (str): Unique identifier for the account.
        owner (str): Name of the account holder.
        balance (float): Current account balance.
        transaction_history (list): List of transaction records.
    """

    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history: List[Dict] = []

    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.
        Args:
            amount (float): Amount to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self._log_transaction("Deposit", amount)

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """Abstract method to withdraw money."""
        pass

    def get_statement(self) -> str:
        """Return a formatted account statement."""
        statement_lines = [
            f"Statement for {self.owner} (Account: {self.account_number})",
            "-" * 50
        ]
        for t in self.transaction_history:
            statement_lines.append(
                f"{t['time']} | {t['type']:10} | {t['amount']:>8.2f} | Balance: {t['balance']:.2f}"
            )
        return "\n".join(statement_lines)

    def _log_transaction(self, transaction_type: str, amount: float) -> None:
        """Record transaction details with timestamp."""
        self.transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "balance": self.balance,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })


class SavingsAccount(Account):
    """
    Savings account with interest calculation.
    """

    def __init__(self, account_number: str, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float) -> None:
        """Withdraw money from savings account if sufficient balance exists."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self._log_transaction("Withdrawal", amount)

    def add_interest(self) -> None:
        """Apply interest to the balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction("Interest", interest)


class CheckingAccount(Account):
    """
    Checking account with overdraft protection.
    """

    def __init__(self, account_number: str, owner: str, balance: float = 0.0, overdraft_limit: float = 500.0):
        super().__init__(account_number, owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        """Withdraw money, allowing overdraft up to the limit."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self.balance -= amount
        self._log_transaction("Withdrawal", amount)



if __name__ == "__main__":
    savings = SavingsAccount("S123", "Kushal", 1000, 0.05)
    checking = CheckingAccount("C456", "Sandeep", 500, 300)

    savings.deposit(200)
    savings.withdraw(100)
    savings.add_interest()

    checking.withdraw(700)  # Overdraft usage

    print(savings.get_statement())
    print()
    print(checking.get_statement())
