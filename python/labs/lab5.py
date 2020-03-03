"""
Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
"""
import random


eyes = [":", "8", ";", "x", "="]
noses = ["^", "*", "-", "<", "o"]
mouths = ["D", "]", "3", "O", "P"]

# y = (random.choice(eyes) + random.choice(noses) + random.choice(mouths))

i= 0 

while i <= 6:
    i = i + 1
    if i == 6:
        break
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    print (eye + nose + mouth)
        
# for i in range (5):
#     eye = random.choice(eyes)
#     nose = random.choice(noses)
#     mouth = random.choice(mouths)
#     print (eye + nose + mouth)
