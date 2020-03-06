# # #Version 1
# # antonym = input ("Give me an antonym for data: ")
# # adjective = input ("Tell me an adjective: ")
# # buzzwood = input ("Give me a sciency buzzword: ")
# # animal = input ("A type of animal (plural): ")
# # sciency = input ("some sciency thing: ")
# # sciency2 = input ("another sciency thing: ")
# # sci_adj = input ("sciency adjective: ")

# # print (f"{antonym} Scientist Job Description: Seeking a {adjective} engineer, able to work on {buzzwood} projects with a team of {animal}. Key responsibilities: Extract patterns from non-material. Optimize {sciency}. Transform {sciency2} into {sci_adj} material.")


# # # Version 2 

# # mad_lib = input("Name 3 adjectives ")
# # answer = mad_lib.split()

# # print (f"My {answer[0]} is {answer[1]} and {answer[2]}! ")




# # import random

# # mad_lib = input("Enter 3 adjectives ")
# # answer = mad_lib.split()

# # print("my", random.choice(answer), "is", random.choice(answer), "the", random.choice(answer), "!" )

# # #Version 3 

antonym = input ("Give me an antonym for data: ")
adjective = input ("Tell me an adjective: ")
buzzwood = input ("Give me a sciency buzzword: ")
animal = input ("A type of animal (plural): ")
sciency = input ("some sciency thing: ")
sciency2 = input ("another sciency thing: ")
sci_adj = input ("sciency adjective: ")

print (f"{antonym} Scientist Job Description: Seeking a {adjective} engineer, able to work on {buzzwood} projects with a team of {animal}. Key responsibilities: Extract patterns from non-material. Optimize {sciency}. Transform {sciency2} into {sci_adj} material.")

question = input ("Do you want to hear the story again? ")


while(question == "yes"):
    antonym = input ("Give me an antonym for data: ")
    adjective = input ("Tell me an adjective: ")
    buzzwood = input ("Give me a sciency buzzword: ")
    animal = input ("A type of animal (plural): ")
    sciency = input ("some sciency thing: ")
    sciency2 = input ("another sciency thing: ")
    sci_adj = input ("sciency adjective: ")
    print(f"{antonym} Scientist Job Description: Seeking a {adjective} engineer, able to work on {buzzwood} projects with a team of {animal}. Key responsibilities: Extract patterns from non-material. Optimize {sciency}. Transform {sciency2} into {sci_adj} material.")
    question = input ("Do you want to hear the story again? ")
    if question == "no":
        print("Goodbye! ")


# Justin's solution

from random import choice

def choose(a_list):
    rand_item = choice(a_list)
    a_list.remove(rand_item) #so you dont get things repeated in your madlib 
    return rand_item #giving it back to the user when they call this function

def main():
    user_input = []

    prompts = [
        '\nGive me an antonym for \'data\': ',
        'Give me a noun: ',
        'Tell me an adjective: ',
        'Give me a sciency buzzword: ', 
    ]

    while True: #true defines an infinite loop
        for prompt in prompts:
            user_input.append(input(prompt))  

        madlib = f'\n{choose(user_input)} scientist job descrition: \
        \nSeeking a {choose(user_input)} engineer, able to work on {choose(user_input)} projects with a team of {choose(user_input)}.'
        # if you hold down alt and clicked all the spots where the curly braces are, you only have to type once.
        
        print(madlib)

        if(input('\n Would you like to make another? (y/n): ').lower() != 'y'): #!= is a boolean which connects to while True
            print("i don\'t blame you. \n")
            break 
main() #calls the function so we can do the prompt. 

# a_list = ["a", "b", "c", "d"]

# print(choice(a_list))



    

 
    







