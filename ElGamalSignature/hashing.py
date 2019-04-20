import hashlib

file = open("Parameters/message.txt", 'r')
message = file.read()
message = message.encode()
hash_object = hashlib.sha256(message)
hex_dig = hash_object.hexdigest()

file = open("Parameters/message.txt", "w")
file.write(str(hex_dig))