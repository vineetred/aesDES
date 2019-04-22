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

def ext_GCD(arg1, arg2):
    prevRemain, remainder = abs(arg1), abs(arg2)
    x, oldX, y, oldY = 0, 1, 1, 0
    while remainder:
        prevRemain, (quotient, remainder) = remainder, divmod(prevRemain, remainder)
        x, oldX = oldX - quotient*x, x
        y, oldY = oldY - quotient*y, y
    return prevRemain, oldX * (-1 if arg1 < 0 else 1), oldY * (-1 if arg2 < 0 else 1)

def inv(e, phi):
    g, x, y = ext_GCD(e, phi)
    if (g != 1):
	    raise Exception("No modular inverse exists")
    posans = (x%phi)
    return posans

def readKeys():
    file = open("Parameters/public_key.txt", 'r')
    global p,g,h,r,signature
    p = int(file.readline())
    g = int(file.readline())
    h = int(file.readline())
    file.close()

    file = open("Parameters/signature.txt",'r')
    r = int(file.readline())
    signature = int(file.readline())

def readMessage():
    file = open("Parameters/message.txt", 'r')
    message = file.read()
    print("Message:",message)
    message_Encrypted = int(binascii.hexlify(message.encode('utf-8')),16)
    global m
    m = message_Encrypted

def verify():
    #Check signature
    g_m = exponent(g,m,p)
    rhs = (exponent(h,r,p)*exponent(r,signature,p))%p
    if(g_m == rhs):
        print("Signature: True")
    else:
        print("Signature: False")

def forged():
    file = open("Parameters/public_key.txt", 'r')
    global p,g,h,r,signature,m
    p = int(file.readline())
    g = int(file.readline())
    h = int(file.readline())
    file.close()

    file = open("Parameters/forged_signature.txt",'r')
    r = int(file.readline())
    signature = int(file.readline())
    file.close()
    file = open("Parameters/message.txt", 'r')
    message = int(file.readline())
    file.close()
    m = message
    print("Message:",m)



readKeys()
readMessage()
#UNCOMMENT THE LINE BELOW WHEN SHOWING EXISTENTIAL FORGERY
# forged()
verify()
