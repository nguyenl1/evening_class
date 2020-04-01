

class ATM:
    def __init__(self, balance=0, print_transactions=[]):
        self.balance = balance
        self.print_transactions=[]

    def check_balance(self):
        return f'your balance is {self.balance}'

    def deposit(self, amount):
        self.balance = self.balance + amount
        string = f'Your balance is now {self.balance}, user has deposited {amount}'
        self.print_transactions.append(string)
        return self.balance 


    def check_withdrawal(self, amount):
        self.withdrawal = self.balance - amount
        if self.withdrawal > 0:
            return True
        else:
            return False

    def withdraw(self, amount):
        self.balance = self.balance - amount
        string = f'Your balance is now {self.balance}, user has withdrew {amount}'
        self.print_transactions.append(string)
        return self.balance
    
    def get_transactions(self):
        return self.print_transactions


    



# print(my_atm.check_balance())
# print(my_atm.deposit(500))
# print(my_atm.check_withdrawal(2000))
# print(my_atm.withdraw(2000))
# print(my_atm.print_transactions())


my_atm = ATM()

while True:
    
    user_input = input ("what would you like to do (deposit, withdraw, check balance, history)? ")

    if user_input == "deposit":
        deposit = int(input("how much would like to deposit? "))
        print(my_atm.deposit(deposit))
    elif user_input == "withdraw":
        withdraw = int(input("How much would you like to withdraw? "))
        print(my_atm.withdraw(withdraw))
    elif user_input == "check balance":
        print(my_atm.check_balance())
    elif user_input == "history":
        print(my_atm.get_transactions())
    cont = input ("Would you like to complete another transaction? (Y/N) ")
    if cont != "Y":
        print ("Goodbye!")
        break


