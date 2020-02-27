# a_string = '\t dobby dies in \n dies in \n book 7'
# print(a_string) #make a rupi kapar poem with this LOL

# a_string = 🤠
# print = (a_string)
# print(ord(a_string)) #gives you emoji code
# print(chr(####)) #prints you emoji 

# strip and split
# s = "      hello there"

# a = s.strip()
# b = s.strip('e')

# print(a)
# print(b)

# c = s.split ()
# print(c)

# d = s.split('e')
# print(d)

# my_string = 'he🤠y!'
# some_char = '🤠'
# if some_char in my_string:
#     print("i found it")
# else: 'it\'s not here man'

# \list

# nums = [3, 5, 2, 3, 45, 23, 42]

# print(nums[0:5]) #slicing
# print(nums[5::-1]) #prints the list backwards
# print (nums[1:5:2]) #2 is what how much you want to skip. 
# print(nums[::-1]) #start at the end and go through it to finish. 


# for each_item in nums:
#     print(each_item)

# print(233 in nums) # in checks if these are in the list.

# print(nums[-2]) 

# x = [3, 4, 5]
# t = [2, 4, 5]

# print(t == x)

#while

# while True:
#     print("zomg stop me!") #infinite loop

# i = 0 
# while i < 10:
#     if i == 5: #conditional
#         print ('woohoo')
#     print(i)
#     i += 1
# print('done')

# i = 0 
# while i < 10:
#     if i == 5: 
#         break
#     print(i)
#     i += 1
# print('done')

# for this item in this group

# text = 'hello world!'
# for char in text:
#     print(char)
    
# fruits = [ 'apples', 'bananas', 'pears', 'cherries', 'pineapples']
# for i in range(len(fruits)):
#     print(fruits[i])

# fruits = [ 'apples', 'bananas', 'pears', 'cherries', 'pineapples']
# for i in range(len(fruits)):
#     if i == 4:
#         break #continue is to skip elements
#     print(fruits[i])

new_list = []
my_flag = True
while my_flag:
    new_list.append("flag")
    if len(new_list) > 4:
        my_flag = False
print(new_list)
