""" Deaundre """ 

import string 

# # """
# # Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.


# # Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# # English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# # ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m



# # english = ["a",	"b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# # rot13 = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a",	"b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

# english =	"abcdefghijklmnopqrstuvwxyz"
# rot13 = "nopqrstuvwxyzabcdefghijklm"

# user_input = input("Insert your code ").lower()

# x = english.rindex(y)
# print(x)

# print(rot13[x::])


#version1

#start with a blank output string
#loop through every character of the string that the user entered
#find the index of that character in the alphabet
#using the index, find the character in the rotated alphabet
#append that character to the output string. 

"""

user_input = input("Insert your code ").lower()

english = [" ", "a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

rot13 = [" ", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a",	"b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

y = ""

for i in user_input: 
    x = english.index(i)
    # print (rot13[x])
    y += rot13[x]

print("".join(y))

"""

#version2

# abc =	"abcdefghijklmnopqrstuvwxyz"
    
abc = string.ascii_lowercase

ABC = string.ascii_uppercase

rotation = int(input("Enter your rotation "))
user_input = input("Insert your code ")


y = ""
for i in user_input:
        x = (abc.index(i) + rotation) % 26
        y += abc[x]

print(y)


y2 = ""
for i in user_input:
    x = (ABC.index(i) + rotation) % 26
    y2 += ABC[x]

print (y2)

for char in string:
    if input is letters: 
        logic 
    else:
        input.append(y)

###



    
x = i1 + i2 + i3 + i4
x = list(x)
random.shuffle(x)
print("".join(x))


# list(user_input)

# y = []

# for i in user_input:
#     x = (abc.index(i) + rotation) % 26
#     y += abc[x]
# 
#   if user_input not in abc:
#         abc.append(y)
#         y = y + i
         

# print("".join(z))

# while True:
#     question = (input("enter a number, or done "))
#     if question == "done":
#         break
#     else:
#         x = int(question)
#         nums.append(x)


"""
slicing

nums = [4, 56, 73, 12, 17, 99, 42, 87]



print(nums[::]) whole string

print(nums[3::]) starts the count at the 4th element

print(nums[2:6:]) start at position 2 and then end at position before the 6th position

print(nums[2:6:2]) start at 2, end before 6th position and skips by 2

print(nums[::2]) skip by 2

print(nums[-1::]) going backwards
 """