from random import randrange, getrandbits, random
import math
import binascii
import sys

file = open("public_key.txt", 'r')


#Change message here
message = "helloworldhelloworld"

print("Message:")
print(message)

message_Encrypted = int(binascii.hexlify(message.encode('utf-8')),16)

m = message_Encrypted
p = int(file.readline())
g = int(file.readline())
h = int(file.readline())

r = randrange(2,(p-1))

cipher_1 = pow(g,r,p)
cipher_2 = pow(h,r,p)

cipher_2 = cipher_2 * m
cipher_2 = cipher_2%p

#Writing to file
file = open("encrypted.txt", "w")
file.write(str(cipher_1) + "\n")
file.write(str(cipher_2))