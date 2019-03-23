import random
def exp_func(x, y):
    exp = bin(y)
    value = x
 
    for i in range(3, len(exp)):
        value = value * value
        if(exp[i:i+1]=='1'):
            value = value*x
    return value

print(exp_func(2,3))

file = open("public_key.txt", 'r')
p = int(file.readline())
g = int(file.readline())
r = random.randrange(2,(p-1))

h = int(file.readline())
# print(exp_func())


print(exp_func(g,r,p))


 