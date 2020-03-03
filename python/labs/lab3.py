"""
Lab 3: Grading
Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

input, print
type conversion (str to int)
comparisons (< <= > >=)
if, elif, else

"""

# enter_grade = int(input("Please enter your grade. "))

# if enter_grade >=90 and enter_grade <= 100:
#     print("You got an A!")
# elif enter_grade >=80 and enter_grade <= 89:
#     print("You got a B! ")
# elif enter_grade >= 70 and enter_grade <= 79:
#     print("You got a C! ")
# elif enter_grade >= 60 and enter_grade <= 69:
#     print("You got a D :(")
# elif enter_grade <= 59:
#     print("Schedule a meeting with your intructor..")

# Version 2

# enter_grade = int(input("Please enter your grade. "))

# if 97 <= enter_grade <= 100:
#     print("You got an A+! ")
# elif 93 <= enter_grade <= 96:
#     print("You got an A! ")
# elif 90 <= enter_grade <= 92:
#     print("You got an A-! ")
# elif 87 <= enter_grade <= 89:
#     print("You got a B+! ")
# elif 83 <= enter_grade <= 86:
#     print("You got a B! ")    
# elif 80 <= enter_grade <= 82:
#     print("You got a B-! ")
# elif 77 <= enter_grade <= 79:
#     print("You got a C+! ")
# elif 73 <= enter_grade <= 76:
#     print("You got a C! ")
# elif 70 <= enter_grade <= 72:
#     print("You got a C-! ")
# elif 67 <= enter_grade <= 69:
#     print("You got a D+! ")
# elif 63 <= enter_grade <= 66:
#     print("You got a D! ")
# elif 60 <= enter_grade <= 62:
#     print("You got a D-! ")
# elif enter_grade <= 59:
#     print("Schedule a meeting with your intructor..")

# Version 3


# s = 'Year is '
# y = 2018
# print(s + str(y))
# print(81%10)


while True:
    grade = int(input("Please enter your grade. "))

    def qualifier ():
        if grade % 10 <= 2:
            qualifier = ("-")
        elif grade % 10 >= 3 and grade %10 <= 7:
            qualifier = (" ")
        elif grade %10 <= 9:
            qualifier = ("+")
        return qualifier
    

    if grade >= 90 and grade <= 100:
        print("Student got A"+ qualifier())

    elif grade >= 80 and grade <= 89:
        print(f"Student got B" + qualifier())

    elif grade >= 70 and grade <= 79:
        print("You got a C! " + qualifier())

    elif grade >= 60 and grade <= 69:
        print("You got a D :(" + qualifier())

    elif grade <= 59:
        print("Schedule a meeting with your intructor..")
        
    if(input('Would you like to input another grade? (y/n): ').lower() != 'y'):
        print(" Goodbye! ")
        break 

        
        




"""
Notes: 
grade = int(input("Please enter your grade. "))

if grade >= 90 and grade <= 100:
    if grade % 10 <= 2:
        qualifier = ("-")
    elif grade % 10 >= 3 and grade %10 <= 7:
        qualifier = (" ")
    elif grade %10 <= 9:
        qualifier = ("+")
    print(f"Student got A{qualifier}")

if grade >= 80 and grade <= 89:
    if grade % 10 <= 2:
        qualifier = ("-")
    elif grade % 10 >= 3 and grade %10 <= 7:
        qualifier = (" ")
    elif grade %10 <= 9:
        qualifier = ("+")
    print(f"Student got B{qualifier}")
"""

