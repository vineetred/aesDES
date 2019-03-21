from random import randrange, getrandbits, random
import math
import binascii

file = open("public_key.txt", 'r')

message = "helloworld"
print("Message:")

message_Encrypted = int(binascii.hexlify(message.encode('utf-8')),16)

print(message)
m = message_Encrypted
q = int(file.readline())
g = int(file.readline())
h = int(file.readline())

r = randrange(2,(q-1))

C_1 = pow(g,r,q)
C_2 = pow(h,r,q)

C_2 = C_2 * m
C_2 = C_2%q

#Writing to file
file = open("encrypted.txt", "w")
file.write(str(C_1) + "\n")
file.write(str(C_2))