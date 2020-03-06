"""
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
"""

import random

# i = input("Do you want to play a game? (yes/no) ")

# while i == "yes":
while True:
    user = input("rock , paper , or scissors? ")

    choice = ["rock", "paper", "scissors"]

    computer = random.choice(choice)

    if  user == computer:
        print(f"Computer got {computer}, it's a tie!")
    elif user == "rock" and computer == "scissors":
        print(f"Computer got {computer}, you win! ")
    elif user == "paper" and computer == "rock":
        print (f"Computer got {computer}, you win!")
    elif user == "scissors" and computer == "paper":
        print (f"Computer got {computer}, you win!" )
    else:
        print("You lose!")

    i = input("Do you want to play again? (yes,no) ")
    if i != "yes":
        print("Goodbye")
        break
    # else:
    #     print("Goodbye!")


# #Justin's solution 

import random 

# created my main function

def main ():
    valid_moves = ["rock", "paper", "scissors"] # created a list of valid moves (rock, paper, scissors)
    winning_cases = [tuple()] # create a list of tuples that represent valid winning cases 

    while True:
    user = input("rock , paper , or scissors? ")
    choice = ["rock", "paper", "scissors"]
    computer = random.choice(choice)
    i = input("Do you want to play again? (yes or q) ") # while the user wants to keep playing, ask the user for a move 
    if i == "q": #if the user chooses "q" i quit
        print("Goodbye")
    else:
        continue



# choose a move for the computer by picking an element out of the valid moves list

# create a tuple out of the users move and the cmoputers move (user's move, computer's move )

# used conditionals to check
#     if the user move is not in valid moves, tell them to try again or quit
#     if the user's move is the same as the computers move, tell them they tied
#     if the tuple (user's move, computer's move') is in the list of tuples that contain the possible combinations of winning moves, tell the user they won
#     else, tell the user theyre a loser and they got beat 



