from random import randrange, getrandbits, random
import math

def possible_Prime(length):
    i = False
    while(i == False):
        num = getrandbits(length)
        if(len(str(num))>=91):
            i = True
    return num


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

q = prime_Generate(300)
p = (2*q)+1

def lucas_Test_new(g, P,Q):
    stable = P
    # print(P)
    # for i in range(2,stable):
    P = int(2)
    # print(P)
    medit = pow(g, P, P)
    if(medit%stable==1):
        return False
    medit = pow(g,Q,P)
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


g = primitive_Root()
g = g*g

a = randrange(2,(q-1))
# print(a)

h = pow(g,a,q)

# print(numberrr)


# def testing():
#     possible = 2
#     result = False
#     numq = 3
#     nump = 7
#     for i in range(0,nump):

#         result = lucas_Test_new(i,nump,numq)
#         print(result)
#     # return possible
#     return result

# numberrr = testing()
# print(numberrr)

#Encryptuon - r
r = randrange(2,(q-1))
C_1 = pow(g,r,q)
C_2 = pow(h,r,q)
m = 101010
C_2 = C_2 * m
C_2 = C_2%q
print(m)
# print(C_1)

t1 = pow(C_1,a,q)
t1inv = inv(t1,q)
t2 = (C_2 * t1inv)%q
print(t2)