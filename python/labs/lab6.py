"""
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
"""
import random 
import string 

# pw_length = int(input ("How long would you like your password? "))
# pw = string.ascii_letters + string.digits + string.punctuation

# i= "" 
# y = 0
# while 0 <= pw_length:
#     y = y + 1
#     i += random.choice(pw)
#     if y == pw_length:
#         break
# print (i)

# Version 3


lower = int(input("How many lowercase letters would you like? "))
password1 = string.ascii_lowercase

i1= "" 
y = 0
while 0 <= lower:
    y = y + 1
    i1 += random.choice(password1)
    if y == lower:
        break


upper = int(input("How many uppercase letters would you like? "))
password2 = string.ascii_uppercase

i2= "" 
y = 0
while 0 <= upper:
    y = y + 1
    i2 += random.choice(password2)
    if y == upper:
        break


num = int(input("How many numbers would you like? "))
password3 = string.digits

i3= "" 
y = 0
while 0 <= num:
    y = y + 1
    i3 += random.choice(password3)
    if y == num:
        break

char = int(input("How many special characters would you like? "))
password4 = string.punctuation

i4= "" 
y = 0
while 0 <= char:
    y = y + 1
    i4 += random.choice(password4)
    if y == char:
        break
x = i1 + i2 + i3 + i4
x = list(x)
random.shuffle(x)
print("".join(x))


    


