from random import randrange, getrandbits, random
import math
import binascii

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
q = int(file.readline())
g = int(file.readline())
h = int(file.readline())
file.close()

file = open("encrypted.txt", 'r')
C_1 = int(file.readline())
C_2 = int(file.readline())
# h = int(file.readline())
file.close()

file = open("private_key.txt","r")
a = int(file.readline())


t1 = pow(C_1,a,q)
t1inv = inv(t1,q)
t2 = (C_2 * t1inv)%q

final_message = binascii.unhexlify(hex(t2)[2:]).decode()
print(final_message)