"""
Problem 1
Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    ...
is_even(5) → False
is_even(6) → True

"""
# def is_even(a):
#     if a%2 != 0:
#         return "True"
#     else:
#         return "False"

# print(is_even(5))
# print(is_even(6))

"""
Problem 2 
Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

def opposite(a, b):
    ...
opposite(10, -1) → True
opposite(2, 3) → False
opposite(-1, -1) → False

"""

def opposite(a,b):
    if a < 0 and b > 0:
        return "True"
    elif a > 0 and b < 0: 
        return "True"
    else: 
        return "False"

print(opposite(-10,-10))

"""
Problem 3 
    
Write a function that returns True if a number within 10 of 100.

def near_100(num):
    ...
near_100(50) → False
near_100(99) → True
near_100(105) → True

"""

# def near_100(num):
#     if num >= 0 and num <= 100:
#         print("True")
#     else:
#         print("False")

# near_100(50)
# near_100(102)

"""
Problem 4
Write a function that returns the maximum of 3 parameters.

def maximum_of_three(a, b, c):
    ...
maximum_of_three(5,6,2) → 6
maximum_of_three(-4,3,10) → 10
""" 

# def maximum_of_three(a, b, c):
#     print(max(a,b,c))


# maximum_of_three(5,2,4)
# maximum_of_three(5,6,2)
# maximum_of_three(-4,3,10)

"""
Problem 5
Print out the powers of 2 from 2^0 to 2^20

1, 2, 4, 8, 16, 32, ...
"""

# def powers(a):
#     2 ** a

def powers():
    x = 0
    print (2 ** 0)
    while True:
        x = x + 1 
        y = 2 ** x 
        if x == 20:
            break
        print(y)

powers()
