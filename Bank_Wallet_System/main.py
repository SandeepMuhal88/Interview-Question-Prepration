import math


class Account:
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        """Read-only balance property."""
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

    def __repr__(self) -> str:
        return f"Account(account_number='{self.account_number}', balance={self.balance})"

    def __len__(self) -> int:
        return math.floor(self._balance)

    def __add__(self, other) -> float:
        if not isinstance(other, Account):
            return NotImplemented

        return float(self.balance + other.balance)


class CheckingAccount(Account):
    def __init__(
        self,
        account_number: str,
        initial_balance: float = 0.0,
        overdraft_limit: float = 100.0
    ):
        super().__init__(account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")

        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded")

        self._balance -= amount

    @property
    def available_funds(self) -> float:
        return self.balance + self.overdraft_limit



acc1 = Account("ACC001", 500.0)
acc2 = Account("ACC002", 300.0)

acc1.deposit(100)
print(acc1.balance)
# 600.0

acc1.withdraw(200)
print(acc1.balance)
# 400.0

print(acc1)
# Account(account_number='ACC001', balance=400.0)

print(len(acc1))
# 400

print(acc1 + acc2)
# 700.0

checking = CheckingAccount(
    "CHK001",
    initial_balance=50.0,
    overdraft_limit=100.0
)

checking.withdraw(120)

print(checking.balance)
# -70.0

print(checking.available_funds)
# 30.0