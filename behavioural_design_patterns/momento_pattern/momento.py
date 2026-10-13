class Momento:
    def __init__(self, balance):
        self.balance = balance

class BankAccount:
    def __init__(self, balance=0) -> None:
        self.balance = balance
        self.changes = [Momento(self.balance)]
        self.current = 0

    def deposit(self, amount):
        self.balance += amount
        self.current += 1
        momento = Momento(self.balance)
        self.changes.append(momento)
        return momento

    def restore(self, momento: None| Momento = None):
        if momento:
            self.balance = momento.balance
            self.changes.append(momento)
            self.current = len(self.changes) - 1

    def undo(self):
        if self.current > 0:
            self.current -= 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def redo(self):
        change_length = len(self.changes)
        if self.current + 1 < change_length:
            self.current += 1
            m = self.changes[self.current]
            self.balance = m.balance
            return m
        return None

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    print(ba)
    m1 = ba.deposit(50)
    print(ba)
    m2 = ba.deposit(25)
    print(ba)
    ba.undo()
    print(ba)
    ba.undo()
    print(ba)
    ba.redo()
    print(ba)
