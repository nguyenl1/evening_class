"""
Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
"""


def anagram (word_one, word_two):
    if sorted(word_one).lower() == sorted(word_two).lower():
        print("This is an anagram")
    else:
        print("This is not an anagram")

word_one = input("Enter the first word: ")
word_two = input("Enter the second word: ")
anagram (word_one, word_two)
