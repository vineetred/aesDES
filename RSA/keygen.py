from random import randrange, getrandbits, random
import sys
import binascii
sys.setrecursionlimit(6000)

def exponent(num,e,n):
    if((e&1)==1):
        remainder = num%n
    else:
        remainder = 1
    e //=2

    while(e>0):
        num = (num*num) % n
        if((e&1)==1):
            remainder = (remainder*num)%n
        e//=2
    return remainder

def possible_Prime(length):
    i = False
    while(i == False):
        num = getrandbits(length)
        if(len(str(num))>=1):
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
        x = exponent(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = exponent(x, 2, n)
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

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_E(phi_n):
    hcf = 0
    while(hcf!=1):
        e = randrange(0,phi_n)
        hcf = gcd(e,phi_n)
    # print("HCF - " + str(hcf))
    return e

def find_D(e, phi):

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

bits = 512

p = prime_Generate(bits)
q = prime_Generate(bits)

n = p*q
phi_n = (p-1)*(q-1)
#Find e
e = find_E(phi_n)
#Find d
d = find_D(e,phi_n)

#Writing to file
file = open("public_key.txt", "w")
file.write(str(e) + "\n")
file.write(str(n))
file = open("private_key.txt","w")
file.write(str(d))