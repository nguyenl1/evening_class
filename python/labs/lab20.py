def get_data():
    cc = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
    return cc

f = get_data()
print(f)

def check_digit(cc):
    check_digit = cc[0:15]
    return check_digit

a = check_digit(get_data())
print(a)

def cc_reverse(a):
    cc_reverse = a[::-1]
    return cc_reverse

b  = cc_reverse(a)
print (b)


def double(b):
    final = []
    i = 0
    while i <= len(b):
        double = b[i] * 2
        final.append(double)
    
        if i+2 > len(b):
            break
    
        final.append(b[i+1])
        i += 2
    
    return final

c = double(b)
print (c)

def nine(c):
    nine = []
    for i in c: 
        if i > 9:
            subtract = i - 9
            nine.append(subtract)
        else:
            nine.append(i)
    print(nine)

d = nine(c)
print (d)

def add(d):
    add = sum(d)
    return add 

e = add(d)
print(e)

def match(e):
    second = str(e)[1]
    last = f[15]
    print (last)
    if int(second) == last:
        print("Valid!")
    else:
        print("jk")




