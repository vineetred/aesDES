import hashlib
mes = "Hello World"
mes = mes.encode()
hash_object = hashlib.sha256(mes)
hex_dig = hash_object.hexdigest()

file = open("hashed_message.txt", "w")
file.write(str(hex_dig))