# x = 5
# y = 5
# print(x is y)

# print(id(x)) #returns ID of an object

# truthy falsey

# empty lists, strings, None is a falsey value

x = []
y = [1,2,3]
i = ""
j = "qwerty"
z = None

if x:
    print(x)
if y:
    print(y) # [1,2,3]
if i:
    print(i)
if j:
    print(j) # qwerty
if z:
    print(z)


# 
my_flag = True
while my_flag: #will always run if the conditio is true.
    print("hey there ")
    user_input = input("do you want to say hi again?")
    if user_input == 'n':
        my_flag = False


my_list = [1,2,3,4,5,6]

for item in my list:
    if item == 4:
        continue
    print(item)

x = 7
y = 34
z = 9 

print(6 < y < 100)