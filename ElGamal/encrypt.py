from random import randrange, getrandbits, random
import math
import binascii
import sys


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

file = open("public_key.txt", 'r')
p = int(file.readline())
g = int(file.readline())
h = int(file.readline())
file.close()

file = open("plaintext.txt", 'r')
message = file.read()

print("Message:")
print(message)

message_Encrypted = int(binascii.hexlify(message.encode('utf-8')),16)

m = message_Encrypted


r = randrange(2,(p-1))

cipher_1 = exponent(g,r,p)
cipher_2 = exponent(h,r,p)

cipher_2 = cipher_2 * m
cipher_2 = cipher_2%p

#Writing to file
file = open("encrypted.txt", "w")
file.write(str(cipher_1) + "\n")
file.write(str(cipher_2))