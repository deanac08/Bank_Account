
class BankAccount:
    accounts = []

    def __init__(self, balance,intRate):
        self.balance = balance
        self.intRate = intRate
        BankAccount.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdrawal(self,amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        print(self.intRate)
        return self

    def yield_interest(self):
        print(self.intRate)
        return self

savings = BankAccount(200, 0.02)
checking = BankAccount(500, 0.07)

savings.deposit(20).deposit(50).deposit(60).withdrawal(10).display_account_info()

checking.deposit(100).deposit(70).withdrawal(10).withdrawal(5).withdrawal(20).withdrawal(10).display_account_info()
