from random import randrange, getrandbits, random
import math
import binascii

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



file = open("public_key.txt", 'r')
p = int(file.readline())
g = int(file.readline())
h = int(file.readline())
file.close()

file = open("encrypted.txt", 'r')
cipher_1 = int(file.readline())
cipher_2 = int(file.readline())
file.close()

file = open("private_key.txt","r")
a = int(file.readline())
file.close()


plainText_1 = exponent(cipher_1,a,p)
plainText_1inv = inv(plainText_1,p)
plainText_2 = (cipher_2 * plainText_1inv)%p

final_message = binascii.unhexlify(hex(plainText_2)[2:]).decode()
print(final_message)
file = open("decryptedtext.txt","w")
# a = int(file.readline())
file.write(final_message)
file.close()