
""" Open the file.""" 

# f = open("pg12296.txt", )
# contents = f.read()
# print(contents)
# f.close()

# try:
#     f = open("pg12296.txt")
#     contents = f.read()
#     print(contents)
# except (IOError, OSError) as e:
#     print(e)
# finally:
#     f.close()

"""lowercase"""
with open('pg12296.txt', 'r') as camps_trails:
    for line in camps_trails:
        line = line.lower()
        print(line)
camps_trails.close()

"""strip punctuation"""

# import string

# chars = string.punctuation
# no_punc = ""
# with open('pg12296.txt', 'r') as camps_trails:
#     for line in camps_trails:
#         line = line.replace(chars, "")
#         print(line)
# camps_trails.close()

"""split into a list of words"""

# with open('pg12296.txt', 'r') as camps_trails:
#     for line in camps_trails:
#         word = line.split(" ")
#         # print (word)
# camps_trails.close()

""" Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count. """

# word_dict = {}

# words = keys
# counts = values 
# print (word.count(keys))


# print ([ [l, word.count(l)] for l in set(word)]) 
# print (dict( (l, word.count(l) ) for l in set(word))) 

"""
Print the most frequent top 10 out with their counts.
"""

# # word_dict is a dictionary where the key is the word and the value is the count
#     words = list(word_dict.items()) # .items() returns a list of tuples
#     words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
#     for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#         print(words[i])

            
