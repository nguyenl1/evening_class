import random
import string 

# def loops():
#     y = 0 
#     y = y + 1
#     if y == 100,000:
#         break

ran = list(string.digits)
balance = 0 

def pick6():
    x = 0
    y = ""
    while x <= 7:
        x = x + 1
        y += random.choice(ran)
        if x == 7:
            cmp = list(y)
            print(cmp)
            break
    
    x1 = 0
    y1 = ""
    while x1 <= 7:
        x1 = x1 + 1
        y1 += random.choice(ran)
        if x1 == 7:
            yours = list(y1)
            print(yours)
            break
        
    balance = 0

    # for x,y in zip(cmp[::], yours[::]):
    #     print (x,y)
    if cmp[0] == yours[0]:
        balance = (balance + 4)
    elif cmp[0] != yours[0]:
        balance = 0
    elif cmp[1] == yours[1]:
        balance = (balance + 7)
    elif cmp[1] != yours[1]:
        balance = 0
    elif cmp[2] == yours[2]:
        balance = (balance + 100)
    elif cmp[2] != yours[2]:
        balance = 0
    elif cmp[3] == yours[3]:
        balance = (balance + 7)
    elif cmp[3] != yours[3]:
        balance = 0
    
    
    print(balance)

            
pick6()




    



