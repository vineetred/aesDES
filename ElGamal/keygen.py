from random import randrange, getrandbits, random
import math

def possible_Prime(length):
    i = False
    while(i == False):
        num = getrandbits(length)
        if(len(str(num))>=91):
            i = True
    return num

# def pow(b,exp,mod):
#     exp_bin = []
#     while exp > 0:
#         exp_bin.append(exp%2)
#         exp/=2
#     final = 1
#     exp_bin = exp_bin[::-1]
#     for binary in exp_bin:
#         if binary == 0:
#             final = (final*final) % mod
#         elif(binary==1):
#             final = (final*final*b) % mod
#     return final

def prime_Check(n, k):
    
    if (n==2 or n==3):
        return True
    elif (n%2==0):
        return False
    # print("Here")
    s, r = 0, (n-1)
    # print("Here")
    while (r %2 == 0):
        s += 1
        r //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

# print(prime_Check(96,5))

def prime_Generate(length):
    flag = False
    prime = 0
    while(flag == False):
        prime = possible_Prime(length)
        flag = prime_Check(prime, 128)
    return prime

def lucas_Test_new(g, P,Q):
    stable = P
    P = int(2)
    medit = pow(g, P, stable)
    if(medit%stable==1):
        return False
    medit = pow(g,Q,stable)
    if(medit%stable==1):
        return False
    return True

def primitive_Root():
    possible = possible_Prime(300)
    result = False
    while(result == False):
        result = lucas_Test_new(possible, p, q)
        possible = possible_Prime(300)
    return possible

def inv(e,phi):
    def ext_GCD(e_KEY, mod_PHI):
        if (e_KEY == 0):
            return (mod_PHI, 0, 1)
        g, y, x = ext_GCD(mod_PHI%e_KEY,e_KEY)
        return (g, x - (mod_PHI//e_KEY) * y, y)

    def modinv(e_KEY, mod_PHI):
        g, x, y = ext_GCD(e_KEY, mod_PHI)
        return x%mod_PHI
    d_key = modinv(e,phi)
    return d_key

flag = False
while(flag==False):
    q = prime_Generate(300)
    p = (2*q)+1
    flag = prime_Check(p,128)

g = primitive_Root() #This is your primitive root
g = g*g
a = randrange(2,(q-1)) #Secret key

h = pow(g,a,p)

#Writing to file
file = open("public_key.txt", "w")
file.write(str(p) + "\n")
file.write(str(g) + "\n")
file.write(str(h))
file = open("private_key.txt","w")
file.write(str(a))

PK = (q,g,h)
SK = a