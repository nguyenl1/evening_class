class ATM:
    def __init__(self, balance):
        self.balance = balance
        # self.deposit = deposit
        # self.withdrawal = withdrawal
        # self.withdraw = withdraw

    def check_balance(self):
        return f'your balance is {self.balance}'

    def deposit(self, amount):
        self.deposit = self.balance + amount
        return self.deposit

    def check_withdrawal(self, amount):
        self.withdrawal = self.balance - amount
        if self.withdrawal > 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.withdraw = self.deposit - amount
        return self.withdraw 

my_atm = ATM(2400)

print(my_atm.check_balance())
print(my_atm.deposit(500))
print(my_atm.check_withdrawal(2000))
print(my_atm.withdraw(2000))

