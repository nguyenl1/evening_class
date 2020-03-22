cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


user_input = []
one = input("What's your first card? ").upper()
two = input("What's your second card? ").upper()
three = input("What's your third card? ").upper()
user_input.append(one)
user_input.append(two)
user_input.append(three)

# def rules(user_input):
nums = []
for i in user_input:
    if i in cards:
        x = cards.index(i)
        nums.append(card_num[x])
a = sum(nums)

if a > 21:
    print (f"{a} Already busted!")
elif a == 21:
    print(f"{a} Blackjack!") 
elif a > 17 and rules(user_input) < 21:
    print(f"{a} Stay")
elif a < 17:
    print (f"{a} Hit")

