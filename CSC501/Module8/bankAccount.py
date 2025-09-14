class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.__balance = balance  # This attribute is hidden from outside access

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self) -> float:
        return self.__balance
