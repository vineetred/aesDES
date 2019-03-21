from random import randrange, getrandbits, random
import math
import binascii

file = open("public_key.txt", 'r')

message = "101010"
print("Message - ")

message_Encrypted = int(binascii.hexlify(message.encode('utf-8')),16)

print(message)
m = message_Encrypted
# m = 10101
print(m)
q = int(file.readline())
g = int(file.readline())
h = int(file.readline())

r = randrange(2,(q-1))

C_1 = pow(g,r,q)
C_2 = pow(h,r,q)

C_2 = C_2 * m
C_2 = C_2%q
