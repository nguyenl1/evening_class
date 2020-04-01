import random


def pick6(): 
    x = 0
    y = []
    while True:
        ran = random.randrange(0,99)
        x = x + 1
        y.append(ran)
        if x == 6:
            return y
            break

# comp = pick6()
# yours = pick6()

def num_matches(comp, yours):

    match = 0

    for i in range(0,6):
        if yours[i] == comp[i]:
            match += 1
        else:
            match += 0 
    return match



def balance(match):
    balance = 0
    new_balance = balance - 2
    if match == 0: 
        new_balance += 0 
    elif match == 1:
        new_balance += 4
    elif match == 2: 
        new_balance += 7
    elif match == 3: 
        new_balance += 100
    elif match == 4:
        new_balance += 50000
    elif match == 5: 
        new_balance += 1000000
    elif match == 6:
        new_balance += 25000000
    return new_balance

# print(balance(num_matches(comp,yours)))



def compare():
    x = 0 
    current_balance = 0
    while True:
        x += 1
        
        comp = pick6()
        yours = pick6()

    
        current_balance = current_balance + balance(num_matches(comp, yours))

        print(f'Winning ticket: {comp}')
        print(f'Your ticket: {yours}')
    

        print(f'Your balance is: ${current_balance}')

        if x == 100:
            break

compare()
