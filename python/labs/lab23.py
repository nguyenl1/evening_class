"""
Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.
"""
"""
Write a phonebook file:

phonebook = {'David': '5551234', 'Alice': '6662345'}
with open('phonebook.txt', 'w') as phone_book_file:
    for name, number in phonebook.items():
        line = f'{name} {number}\n'
        phone_book_file.write(line)
Read a phonebook file:

with open('phonebook.txt') as phone_book_file:
    phone_book_data = phone_book_file.read().split('\n')

phone_book = {}
for line in phone_book_data:
    name, number = line.split()
    phone_book[name] = number
"""



# import csv 

# # with open('lab23.csv', 'r') as file:
# #     lines = file.read().split('\n')
# #     print(lines)

# with open('lab23.csv', 'r') as file:
#     read = csv.DictReader(file, delimiter=',')
#     for row in read:
#         print(row)


"""
Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.
"""

# name = input("Enter your name. ")
# fav_fruit = input("Enter your your favorite fruit. ")
# fav_color = input("Enter your your favorite color. ")

# phonebook = []

# while True:
#     name = input("Enter your name. ")
#     fav_fruit = input("Enter your your favorite fruit. ")
#     fav_color = input("Enter your your favorite color. ")
#     phonebook.append({
#         "name": name,
#         "fav_fruit": fav_fruit,
#         "fav_color": fav_color
#     })

#     cont = input("Want to add another? Y/N ")
#     if cont != "Y":
#         break

# print(phonebook)


#https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/

#modules
from csv import writer
import csv 

#functions
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

#variables 
phonebook = []
row_count = 0
# open csv, set up dictionary
with open('lab23.csv', 'r') as file:
    read = csv.reader(file, delimiter=',')
    for row in read:
        print(row)

        if row_count == 0:
            row_count+=1
        else: 
            phonebook.append(
                {'name': row[0],
                'favorite fruit': row[1],
                'favorite color': row[2]
                }
            )

print(f"Phonebook: {phonebook}")

while True:
    name = input("Enter your name. ")
    fav_fruit = input("Enter your your favorite fruit. ")
    fav_color = input("Enter your your favorite color. ")

    phonebook.append(
        {'name': row[0],
        'favorite fruit': row[1],
        'favorite color': row[2]
        })

    cont = input("Want to add another? Y/N ")
    if cont != "Y":
        break

print(phonebook)

# Append a list as new line to an old csv file
# append_list_as_row('lab23.csv', phonebook)

# with open('lab23.csv', 'r') as file:
#     read = csv.DictReader(file, delimiter=',')
#     for row in read:
#         print(row)
#         phonebook["name"] = row[0]
#         phonebook["fav_fruit"] = row[1] #can you use an underscore? 
#         phonebook["fav_color"] = row[2]

# print(phonebook)


