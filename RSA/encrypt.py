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

file = open("public_key.txt", 'r')
e = int(file.readline())
n = int(file.readline())
file = open("plaintext.txt", 'r')
msg = file.read()

message_Encrypted = exponent(int(binascii.hexlify(msg.encode('utf-8')),16),e,n) #Converting to hex so that one can encode letters too

file = open("ciphertext.txt", 'w')
file.write(str(message_Encrypted).strip())