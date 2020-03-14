import string

ABC = string.ascii_uppercase
abc = string.ascii_lowercase

rotation = int(input("Enter your rotation "))
user_input = input("Insert your code ")

input = list(user_input)

y = []

for i in input:
    y = y + input
    if input in ABC:
        x = (ABC.index(i) + rotation) % 26
        y += ABC[x]
    elif input in abc:
        x = (abc.index(i) + rotation) % 26
        y += abc[x]
    else:
        y.append(input)
        
print(string(y))


#Deaundre 

import string

alphabet = list(string.ascii_lowercase)
user_input = input("Enter your code: ")
rotation = int(input("Enter the rotation: "))

rot = [alphabet[(alphabet.index(i) + rotation) % 26] if i in alphabet else i for i in sentence] 

rot = "".join(rot)

print (rot)
