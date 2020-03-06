
user_input = int(input("Enter your amount in pennies "))

pennies = 1
nickles = 5 
dime = 10
quarters = 25

quart = user_input//quarters #115//24 = 4 
print(f"{quart} quarters")
di = (user_input%quarters)//dime  
print(f" {di} dimes")
nick = ((user_input%quarters)%dime)//nickles
print (f" {nick} nickles")
pen = (((user_input%quarters)%dime)%nickles)//pennies
print (f" {pen} pennies")

# Version 2 

# user_input = float(input("Enter your dollar amount "))

# pennies = user_input * 100

# print(f"{pennies} pennies")



