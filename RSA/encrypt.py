import binascii


file = open("public_key.txt", 'r')
e = int(file.readline())
n = int(file.readline())

file = open("plaintext.txt", 'r')
msg = file.read()

message_Encrypted = pow(int(binascii.hexlify(msg.encode('utf-8')),16),e,n)
# message = int(message, 16)
# message_Encrypted = pow(message, e, n)

file = open("ciphertext.txt", 'w')
file.write(str(message_Encrypted).strip())