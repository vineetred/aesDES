# Cryptographic Implementations

Simple implementation of RSA and ElGamal.

## RSA 
1. Language = Python 3.6.4
2. To run the program, we have to first generate our public and private keys. To do this, just run the command
"python3 keygen.py".
3. After this, two text files would have been created, public_key and private_key. These contain your keys.
4. The plaintext text file contains the text that needs to be encrypted. Edit this to whatever you like. 
5. To encrypt, just run the command "python3 encrypt.py".
6. To decrypt, run the command "python3 decrypt.py".
7. Make sure the number of bits of the message is smaller than 1024.
8. The decrypted text can be found in the terminal as well as in the file called decryptedtext.txt

## ElGamal
1. Language = Python 3.6.4
2. To run the program, we have to first generate our public and private keys. To do this, just run the command
"python3 keygen.py".
3. After this, two text files would have been created, public_key and private_key. These contain your keys.
4. The plaintext text file contains the text that needs to be encrypted. Edit this to whatever you like. 
5. To encrypt, just run the command "python3 encrypt.py".
6. To decrypt, run the command "python3 decrypt.py".
7. Make sure the number of bits of the message is smaller than 1024.
8. The decrypted text can be found in the terminal as well as in the file called decryptedtext.txt

## RSA Factoring
1. Language = Python 3.6.4
2. Change the values of e, d and n in the file, misc/factoring.py
3. Run the command, "python3 factoring.py"

## References for code
1. Dhruv Agarwal, Vidur Singh and TS Harikrishnan - Code References
2. https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
3. https://rosettacode.org/wiki/RSA_code
4. https://gist.github.com/JonCooperWorks/5314103 - A medium blog post repo
5. https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python - Miller Rabin