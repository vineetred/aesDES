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
cipher_1 = int(file.readline())
cipher_2 = int(file.readline())
file.close()

file = open("private_key.txt","r")
a = int(file.readline())


plainText_1 = pow(cipher_1,a,q)
plainText_1inv = inv(plainText_1,q)
plainText_2 = (cipher_2 * plainText_1inv)%q

final_message = binascii.unhexlify(hex(plainText_2)[2:]).decode()
print(final_message)