import binascii

file = open("private_key.txt", 'r')
d = int(file.readline())
file = open("ciphertext.txt", 'r')
message = int(file.read().strip())
# message = mess
file = open("public_key.txt", 'r')
e = int(file.readline())
n = int(file.readline())
final_Message = str(binascii.unhexlify(hex(pow(message, d, n))[2:]).strip().decode('utf-8'))

# final_Message = pow(message, d, n)
# print('message  ', binascii.unhexlify(hex(final_Message)[2:]).decode('utf-8')) 
print(final_Message)

file = open("decryptedtext.txt", 'w')
file.write(str(final_Message).strip())