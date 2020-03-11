#Version 1 

user_input = input("What is the operation you'd like to perform? ")
first_num = float(input("What is the first number? "))
second_num = float(input("What is the second number? "))

# if user_input == "+":
#     total = first_num + second_num
#     print (f"{first_num} + {second_num} = {total}")
# elif user_input == "-":
#     total = first_num - second_num
#     print (f"{first_num} - {second_num} = {total}")
# elif user_input == "*":
#     total = first_num * second_num
#     print (f"{first_num} * {second_num} = {total}")
# elif user_input == "/":
#     total = first_num / second_num
#     print (f"{first_num} / {second_num} = {total}")

# Version 2

while True:

    user_input = input("What is the operation you'd like to perform? (or done) ")

    if user_input == "done":
        print("Goodbye!")
        break

    first_num = float(input("What is the first number? "))
    second_num = float(input("What is the second number? "))

    
    if user_input == "+":
        total = first_num + second_num
        print (f"{first_num} + {second_num} = {total}")
    elif user_input == "-":
        total = first_num - second_num
        print (f"{first_num} - {second_num} = {total}")
    elif user_input == "*":
        total = first_num * second_num
        print (f"{first_num} * {second_num} = {total}")
    elif user_input == "/":
        total = first_num / second_num
        print (f"{first_num} / {second_num} = {total}")

# Version 3

# user_input = input("Enter a full arithmetic expression ")

# x = user_input
# print(eval(x))

