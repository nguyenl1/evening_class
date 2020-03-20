"""

Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings.

"""

noindex = [0,1,2,3,4,5,6,7,8,9]
tens = [" ", " ", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens = ["ten", "eleven", "twelve", "thirteen", "forteen", "fifthteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ones = [" ","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
hundreds = [" ", "one hundred and ", "two hundred and ", "three hundred and ", "four hundred and ", "five hundred and", "six hundred and ", "seven hundred and ", "eight hundred and ", "nine hundred and "]


user_input = int(input("Enter a number or a roman numeral "))


def eng():
    if user_input > 9 and user_input < 20:
        teen_digit = user_input%10
        x = noindex.index(teen_digit)
        teen = teens[x]
        print (teen)
    elif user_input == 0:
        print("zero")
    elif user_input > 0 and user_input < 100:
        tens_digit = user_input//10
        x = noindex.index(tens_digit)
        ten = tens[x]

        ones_digit = user_input%10
        x = noindex.index(ones_digit)
        one = ones[x]

        print (ten + one)
    elif user_input > 99 and user_input < 1000:
        hundred_index = user_input//100
        x = noindex.index(hundred_index)
        hundred = hundreds[x]
        tens_digit = (user_input%100)//10
        x = noindex.index(tens_digit)
        ten = tens[x]
        ones_digit = (user_input%100)%10
        x = noindex.index(ones_digit)
        one = ones[x]
        print (hundred + ten + one)


eng()







