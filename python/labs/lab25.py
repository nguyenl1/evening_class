transaction = []

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return f'your balance is {self.balance}'

    def deposit(self, amount):
        self.deposit = self.balance + amount
        string = f'user has deposited {self.deposit}'
        transaction.append(string)
        return string


    def check_withdrawal(self, amount):
        self.withdrawal = self.balance - amount
        if self.withdrawal > 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.withdraw = self.deposit - amount
        string = f'user has withdrew {self.withdraw}'
        transaction.append(string)
        return string
    
    def print_transactions(self):
        return transaction


    

my_atm = ATM(2400)

print(my_atm.check_balance())
print(my_atm.deposit(500))
print(my_atm.check_withdrawal(2000))
print(my_atm.withdraw(2000))
print(my_atm.print_transactions())



