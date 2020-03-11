import random

# VERSION 1 

# y = 0 
# while True:
#     user_guess = int(input("Please guess a number "))

#     computer = random.randint(1,10)

#     if user_guess == computer:
#         print("You got it!")
#         break
#     else:
#         print(f"Computer got {computer}, try again ")

#     y = y + 1
#     print (f"You have {y} guesses")
#     if y == 10:
#         print("No more guesses! Goodbye")
#         break

# VERSION 2

# y = 0 

# while True:
#     y = y + 1

#     user_guess = int(input("Please guess a number (Press 0 to exit) "))


#     computer = random.randint(1,10)

#     if user_guess == computer:
#         print("You got it!")
#         break
#     elif user_guess == 0:
#         print(f"You guessed {y} times! Goodbye")
#         break 
#     else:
#         print(f"Computer got {computer}, try again ")

# VERSION 3

# while True:
    
#     user_guess = int(input("Please guess a number "))

#     computer = random.randint(1,10)

#     if user_guess > computer:
#         print("Too high!")
#     elif user_guess < computer:
#         print("Too low!") 
#     else:
#         print("You got it! ")
#         break 

# VERSION 4 
"""
Tell the user whether their current guess is closer than their last. 

This can be done by maintaining a variable containing the last guess outside the loop

then comparing the last guess to the current guess and check if it's closer.

Hint: you're interested in comparing the two absolute differences: 

abs(current_guess-target) and abs(last_guess-target).
abs = l x - y l 

"""

last_guess = 0 

def compare (): 
    
    if current_guess == computer: 
        print("You got it! ")
    elif current_guess != computer:
        print("Try again! ")
        x = abs(current_guess - computer)
        y = abs(last_guess - computer)
        if x < y: 
            print ("You're getting warmer")
        else:
            print ("You're getting colder")
    

computer = random.randint(1,10)

while True:
    current_guess = int(input("Please guess a number "))
    compare()
    last_guess = current_guess



# #VERSION 5

# # y = 0 
# # while True:
# #     user_guess = int(input("Will the computer guess your number? Let's find out. Enter a number. "))

# #     computer = random.randint(1,10)

# #     if computer == user_guess:
# #         print("Computer guessed it, you lose! ")
# #         break
# #     else:
# #         print(f"Computer got {computer}, you win! ")
        










