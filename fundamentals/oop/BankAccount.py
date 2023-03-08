class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []

    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.balance)
            print(account.int_rate)
        return cls

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if(self.balance < amount):
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        print(self.int_rate)
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        else:
            print('Balance is negative')
        return self

account_1 = BankAccount(.01, 500)
account_2 = BankAccount(.04, 6200)

account_1.deposit(200).deposit(400).deposit(627).withdraw(60).yield_interest().display_account_info()
account_2.deposit(40).deposit(300).withdraw(20).withdraw(1000).withdraw(40).withdraw(400).yield_interest().display_account_info()
BankAccount.display_all_accounts()