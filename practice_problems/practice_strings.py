"""
Get a string from the user, print out another string, doubling every letter.
"""

# def double():
#     x = input("Enter a word ")
#     for i in x: 
#         y = i * 2
#         print(y, end= "")
        
# double()

"""
Write a function that takes a string, and returns a list of strings, each missing a different character.
"""

# def missing_char():
#     x = input("Enter a word ")
#     for i in x: 
#         y = x.replace(i,"")
#         print(y)

# missing_char()

"""
Return the letter that appears the latest in the english alphabet.
"""
import string

def latest():
    x = string.ascii_lowercase
    a = list(x)
    user_input = input("Enter a word. ").lower()

    latest = []
    
    for i in user_input:
        if i in a:
            y = a.index(i)
            latest.append(y)
    b = max(latest)
    print(x[b])
            
            
latest()

