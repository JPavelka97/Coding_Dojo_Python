class BankAccount:

    all_accounts = []

    def __init__(self, account_number, int_rate, balance=0): 
        self.int_rate = int_rate
        self.account_number = account_number
        self.balance = balance
        BankAccount.all_accounts.append(self)

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
        print(self.account_number)
        print(self.balance)
        print(self.int_rate)
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        else:
            print('Balance is negative')
        return self

    @classmethod
    def display_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.account_number)
            print(account.balance)
            print(account.int_rate)
        return cls

class User:
    def __init__(self, name, email, account_number, savings_number=None):
        self.name = name
        self.email = email
        self.account = BankAccount(account_number, int_rate=0.02, balance=0)
        self.account2 = BankAccount(savings_number, int_rate=0.08, balance=340)

    def make_deposit(self, amount, account_number):
        if account_number == self.account.account_number:
            self.account.deposit(amount)
            return self
        elif account_number == self.account2.account_number:
            self.account2.deposit(amount)
            return self
        
    def transfer_money(self, amount, other_user):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)


    def make_withdrawal(self, amount, account_number):
        if account_number == self.account.account_number:
            self.account.withdraw(amount)
            return self
        elif account_number == self.account2.account_number:
            self.account2.withdraw(amount)
            return self

    def display_user_balance(self):
        print(self.account.account_number)
        print(self.account.balance)
        print(self.account.int_rate)

        print(self.account2.account_number)
        print(self.account2.balance)
        print(self.account2.int_rate)
        return self

account_Jacob = User('Jacob', 'jacob@gmail.com', 12341234, 50505050)
account_Jacob.make_deposit(300, 12341234)

account_Alfie = User('Alfonse', 'thatsmybrother@gmail.com', 5900, 6000)
account_Alfie.make_deposit(300, 6000)

account_Jacob.transfer_money(200, account_Alfie)
account_Jacob.display_user_balance()
print()
account_Alfie.display_user_balance()



# account_2 = BankAccount(.04, 6200)

# account_1.deposit(200).deposit(400).deposit(627).withdraw(60).yield_interest().display_account_info()
# account_2.deposit(40).deposit(300).withdraw(20).withdraw(1000).withdraw(40).withdraw(400).yield_interest().display_account_info()
# BankAccount.display_all_accounts()