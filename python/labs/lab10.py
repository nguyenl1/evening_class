

# nums = [5, 0, 8, 3, 4, 1, 6]

# add = ( nums[0] + nums [1] + nums [2] + nums [3] + nums [4]+ nums [5]+ nums [6] )

# length = (len(nums))

# avg = add / length

# print (avg)

# Version 1

x = 0
for num in nums:
    x = x + num
    print (x) 

length = (len(nums))

avg = x / length

print (f"The average of the list is {avg}")

# Version 2

nums = [5, 0, 8, 3, 4, 1, 6]

while True:
    question = (input("enter a number, or done "))
    if question == "done":
        break
    else:
        x = int(question)
        nums.append(x)

# questions = list(question)
# questions.append(questions)
    
# new_list = nums + questions

x = 0
for num in nums:
    x = x + num

print(f"Sum is {x}")

length = (len(nums))

print (f"Count is {length}")

avg = x / length

print (f"The average is {avg}")