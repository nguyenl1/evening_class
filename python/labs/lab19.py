import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


user_input = []
one = input("What's your first card? ").upper()
two = input("What's your second card? ").upper()
three = input("What's your third card? ").upper()
user_input.append(one)
user_input.append(two)
user_input.append(three)

nums = []
for i in user_input:
    if i in cards:
        x = cards.index(i)
        nums.append(card_num[x])
    else:
        print("invalid card")
a = sum(nums)

while True:
    if a > 21:
        print (f"{a} Already busted!")
        break
    elif a == 21:
        print(f"{a} Blackjack!") 
        break
    elif a > 17 and a < 21:
        print(f"{a} Stay")
        break
    elif a < 17:
        print (f"{a} Hit")
        hit = random.choice(cards)
        
    for i in hit:
        if i in cards:
            x = cards.index(i)
            b = card_num[x]
            a = (a+b)       

#Version 2

import random

cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


user_input = []
one = input("What's your first card? ").upper()
two = input("What's your second card? ").upper()
three = input("What's your third card? ").upper()
user_input.append(one)
user_input.append(two)
user_input.append(three)

nums = []
for i in user_input:
    if i in cards:
        x = cards.index(i)
        nums.append(card_num[x])
    else:
        print("invalid card")

for i in nums: 
    if i == 1:
        nums.pop(nums.index(i))
        total = sum(nums)
        if total >= 11: 
            ace = 1 
            new_total = ace + total
        
        elif total < 11:
            ace = 11
            new_total = ace + total
print (new_total)

while True:
    if new_total > 21:
        print (f"{new_total} Already busted!")
        break
    elif new_total == 21:
        print(f"{new_total} Blackjack!") 
        break
    elif new_total > 17 and new_total < 21:
        print(f"{new_total} Stay")
        break
    elif new_total < 17:
        print (f"{new_total} Hit")
        break
        

#computer play  

# import random

# cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# def your_cards():
#     hand = random.choice(cards)
#     return hand

# def hit():
#     hit = your_cards()
#     return (hit)

# x = 0 
# user_input = []
# while True:
#     x += 1
#     user_input.append(your_cards())
#     if x == 3:
#         print(user_input)
#         break


# nums = []
# for i in user_input:
#     if i in cards:
#         x = cards.index(i)
#         nums.append(card_num[x])
#     else:
#         print("invalid card")


# def main(): 
#     a = sum(nums)
#     while True:
#         if a > 21:
#             print (f"{a} Already busted!")
#             break
#         elif a == 21:
#             print(f"{a} Blackjack!") 
#             break
#         elif a > 17 and a < 21:
#             close = input(f" you got {a}, hit or stay? ")
#             if close == "hit":
#                 hit()     
#             else:
#                 break
#         elif a < 17:
#             under = input(f" You got {a} do you want to hit? ")
#             if under == "yes":
#                 hit()
#         for i in hit():
#             if i in cards:
#                 x = cards.index(i)
#                 b = card_num[x]
#                 a = (a+b)  

# main()
