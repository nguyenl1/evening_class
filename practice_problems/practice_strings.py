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
# import string

# def latest():
#     x = string.ascii_lowercase
#     a = list(x)
#     user_input = input("Enter a word. ").lower()

#     latest = []
    
#     for i in user_input:
#         if i in a:
#             y = a.index(i)
#             latest.append(y)
#     b = max(latest)
#     print(x[b])
            
            
# latest()

"""
Write a function that returns the number of occurances of 'hi' in a given string.
"""

# def count_hi():
#     li = []
#     user_input = input("enter hi. ")
#     for i in range(0, len(user_input), 2): #(start, end, every 2nd letter)
#         #print(i)
#         out = user_input[i:i+2] #print [i = start value, i+2 = end value] of the user_input. Start with print [0,1] = "hi"
#         #print(out)
#         li.append(out)
#     print(li.count("hi"))
    
# count_hi()

"""
Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'
"""

# def cat_dog():
#     li = []
#     user_input = input("enter catdog. ")
#     for i in range(0, len(user_input), 3):
#         out = user_input[i:i+3]
#         li.append(out)
#     x = li.count("cat")
#     y = li.count("dog")
#     if x == y:
#         print("True")
#     else:
#         print(f" There's {x} cats and {y} dogs. False")
    
# cat_dog()

"""
Return the number of letter occurances in a string.
"""

# def count_letters(letter,word):
#     li = []
#     for i in word: 
#         li.append(i)
#     return li.count(letter)

# print(count_letters('i', 'antidisestablishmentterianism'))

"""
Convert input strings to lowercase without any surrounding whitespace.
"""

# def lower_case():
#     x = input("enter a word. ").lower()
#     print(x.strip())

# lower_case()


"""
Write a function that takes a string, and returns a list of strings, each missing a different character.
"""

# def missing_char():
#     x = input("Enter a word ")
#     for i in x: 
#         y = x.replace(i,"")
#         print(y)

# missing_char()

def missing_char():
    x = input("Enter a word ")
    final = []
    i = 0
    for i in x:
        final.append(x[i])
        print(final.replace(i,""))
        i += 1

missing_char()
        



def double(b):
    final = []
    i = 0
    while i <= len(b):
        double = b[i] * 2
        final.append(double)
    
        if i+2 > len(b):
            break
    
        final.append(b[i+1])
        i += 2
    
    return final