# from random import randrange, getrandbits, random

# def possible_Prime(length):
#     i = False
#     while(i == False):
#         num = getrandbits(length)
#         if(len(str(num))>=1):
#             i = True
#     return num


# def prime_Check(n, k):
    
#     if (n==2 or n==3):
#         return True
#     elif (n%2==0):
#         return False
#     # print("Here")
#     s, r = 0, (n-1)
#     # print("Here")
#     while (r %2 == 0):
#         s += 1
#         r //= 2

#     for _ in range(k):
#         a = randrange(2, n - 1)
#         x = pow(a, r, n)
#         if x != 1 and x != n - 1:
#             j = 1
#             while j < s and x != n - 1:
#                 x = pow(x, 2, n)
#                 if x == 1:
#                     return False
#                 j += 1
#             if x != n - 1:
#                 return False
#     return True

# # print(prime_Check(96,5))

# def prime_Generate(length):
#     flag = False
#     prime = 0
#     while(flag == False):
#         prime = possible_Prime(length)
#         flag = prime_Check(prime, 128)
#     return prime

# # print(prime_Generate(5))
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
import sys
sys.setrecursionlimit(1500)

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
print(find_D(5,72))