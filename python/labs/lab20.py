cc = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

# check_digit = len(cc)
check_digit = cc[0:15]
cc_reverse = check_digit[::-1]


print(check_digit)
print(cc_reverse)

final = []
i = 0 
while i <= len(cc_reverse):
    double = cc_reverse[i] * 2
    final.append(double)
    
    if i+2 > len(cc_reverse):
        break
    
    final.append(cc_reverse[i+1])
    i += 2
    
print(final)

nine = []
for i in final: 
    if i > 9:
        subtract = i - 9
        nine.append(subtract)
    else:
        nine.append(i)
print(nine)

add = sum(nine)
print(add)

second = str(add)[1]
last = cc[15]
print(last)
if int(second) == last:
    print("Valid!")
else:
    print("jk")


