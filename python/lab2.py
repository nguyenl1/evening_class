#Version 1
antonym = input ("Give me an antonym for data: ")
adjective = input ("Tell me an adjective: ")
buzzwood = input ("Give me a sciency buzzword: ")
animal = input ("A type of animal (plural): ")
sciency = input ("some sciency thing: ")
sciency2 = input ("another sciency thing: ")
sci_adj = input ("sciency adjective: ")

print (f"{antonym} Scientist Job Description: Seeking a {adjective} engineer, able to work on {buzzwood} projects with a team of {animal}. Key responsibilities: Extract patterns from non-material. Optimize {sciency}. Transform {sciency2} into {sci_adj} material.")


# Version 2 

mad_lib = input("Name 3 adjectives ")
answer = mad_lib.split()

print (f"My {answer[0]} is {answer[1]} and {answer[2]}! ")




import random

mad_lib = input("Enter 3 adjectives ")
answer = mad_lib.split(', ')

print("my", random.choice(answer), "is", random.choice(answer), "the", random.choice(answer), "!" )

#Version 3 

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
     
    

    

 
    







