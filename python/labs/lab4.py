"""
Print a welcome screen to the user.
Use the random module's random.choice() to choose a prediction.
Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
Display the result of the 8-ball.
"""

from random import choice

while True:

    predictions = ["it is certain", "very doubtful", "concentrate and ask again", "signs point to yes", "don't count on it."]

    user_input = input("Please ask your question ")

    print(choice(predictions))
    
    if(input('Would you like to play again (y/n): ').lower() != 'y'):
        print(" Goodbye! ")
        break 


