from abc import ABC
from enum import Enum
import unittest


class BankAccount:
    OVERDRAFT_LIMIT = -500
    def __init__(self, balance=0) -> None:
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount} balance = {self.balance}")
            return True
        return False

    def __str__(self) -> str:
        return f"balance = {self.balance}"


class Command(ABC):
    def __init__(self) -> None:
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass

class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1

class BankAccountCommand(Command):
    def __init__(self, account, action, amount):
        self.amount = amount
        self.action = action
        self.account = account
    
    def invoke(self):
        if self.action == Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == Action.WITHDRAW:
            self.account.deposit(self.amount)



class CompositeBankAccountCommand(Command, list):
    def __init__(self, items: list[Command] | None = None) -> None:
        if items is None:
            items = []
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_account: BankAccount, to_account: BankAccount, amount: int) -> None:
        super().__init__([
            BankAccountCommand(from_account, Action.WITHDRAW, amount),
            BankAccountCommand(to_account, Action.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok

    def undo(self):
        for x in reversed(self):
            x.undo()


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        deposit1 = BankAccountCommand(ba, Action.DEPOSIT, 100)
        deposit2 = BankAccountCommand(ba, Action.DEPOSIT, 50)
        composite = CompositeBankAccountCommand([deposit1, deposit2])
        print(ba)
        composite.invoke()
        print(ba)
        composite.undo()
        print(ba)

    def test_transfer_fails(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()
        amount = 100
        withdraw = BankAccountCommand(ba1, Action.WITHDRAW, amount)
        deposit = BankAccountCommand(ba2, Action.DEPOSIT, amount)
        transfer = CompositeBankAccountCommand([withdraw, deposit])
        transfer.invoke()
        print(f"account1: {ba1} account2: {ba2}")
        transfer.undo()
        print(f"account1: {ba1} account2: {ba2}")


if __name__ == "__main__":
    # ba = BankAccount()
    # cmd = BankAccountCommand(ba, Action.DEPOSIT, 100)
    # cmd.invoke()
    # print(ba)
    # cmd.undo()
    # print(ba)
    # illegal_cmd = BankAccountCommand(ba, Action.WITHDRAW, 1000)
    # illegal_cmd.invoke()
    # print(ba)
    # illegal_cmd.undo()
    unittest.main()