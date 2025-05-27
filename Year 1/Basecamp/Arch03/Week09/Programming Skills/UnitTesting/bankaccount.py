class BankAccount:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True


def test_sufficient_funds_on_withdraw():
    client1 = BankAccount("Telmo")
    assert client1.deposit(10)
    assert client1.withdraw(5)
