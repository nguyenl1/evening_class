import csv

#version 1 


phonebook = []
row_count = 0
# open csv, set up dictionary
with open('lab23.csv', 'r') as file:
    lines = file.read().split('\n')
    print (lines)
    # for row in lines:

    #     if row_count == 0:
    #         row_count+=1
    #     else: 
    #         phonebook.append(
    #             {'name': row[0],
    #             'favorite fruit': row[1],
    #             'favorite color': row[2]
    #             }
    #         )
    for row in lines: 
        if row_count == 0:
            row_count += 1
        else:
            phonebook.append(row[0])
            phonebook.append(row[1])
            phonebook.append(row[2])
            row_count += 1

print(f"Phonebook: {phonebook}")

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

# user_input = input("who's name do you want to look up? ")

# with open('lab23.csv', 'r') as phone_book_file:
#     for line in phone_book_file:
#         print(line)
#         # if user_input == line[0]:
#         #     print(line)
#         # else:
#         #     print("cant find")

