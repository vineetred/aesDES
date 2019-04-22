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

file = open("private_key.txt", 'r')
d = int(file.readline())
file = open("ciphertext.txt", 'r')
message = int(file.read().strip())
# message = mess
file = open("public_key.txt", 'r')
e = int(file.readline())
n = int(file.readline())
final_Message = str(binascii.unhexlify(hex(exponent(message, d, n))[2:]).strip().decode('utf-8'))
print(final_Message)

file = open("decryptedtext.txt", 'w')
file.write(str(final_Message).strip())