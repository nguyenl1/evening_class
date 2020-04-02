import csv

#version 1 

phonebook = []
with open('lab23.csv') as file:
    read = csv.DictReader(file, delimiter=',')
    for row in read:
        phonebook.append(row)
    print(phonebook)

#version2

"""Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered."""


# phonebook = []
# while True:
#     name = input("Enter your name. ")
#     fav_fruit = input("Enter your your favorite fruit. ")
#     fav_color = input("Enter your your favorite color. ")

#     phonebook.append({
#         'name': name,
#         'fav_fruit': fav_fruit, 
#         'fav_color': fav_color})

#     with open('lab23.csv', 'a') as csv_file:
#             writer = csv.writer(csv_file, delimiter = ',')
#             row = [name,fav_fruit,fav_color]
#             writer.writerow(row)

#     cont = input("Want to add another? Y/N ")
#     if cont != "Y":
#         break

# print(phonebook)

"""Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information"""

phonebook = []
with open('lab23.csv') as file:
    read = csv.DictReader(file, delimiter=',')
    for row in read:
        phonebook.append(row)
    print(phonebook)

user_input = input("Please enter the name of the person you would information of. ").lower()

for row in phonebook:
    if row['name'] == user_input:
        print(row)
   

