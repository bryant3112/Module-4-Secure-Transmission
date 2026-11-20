Module 4 Midterm - Secure Data Transmission

Project Overview
For this project, I created a simple Python program that allows a user to enter a message and protect it using hashing and encryption. The program uses SHA-256 to create a hash and AES-256 to encrypt the message. it then decrypts the message and compares the hashes to make sure the original information has not changed 

How My Program Works
1.- The user enters a message.
2.- The program displays the original message. 
3.- SHA-256 creates a hash of the message
4.- AES-256 encrypts the message using a randomly generated key. 
5.- The program decrypts the message back to its original form
6.- The program compares the hashes to check that the message has not changed.

Confidentiality: Integrity, and Availability
Confidentiality: AES-256 encryption helps keep the message private because someone without the correct key cannot easily read the encrypted information.

Integrity: SHA-256 creates a hash of the original message. after decryption, the program creates another hash and compares them to check if the message has changed. AES-GCM also checks whether encrypted data has been modified.

Availability: The program ncan be used locally as long as Python and the required library are installed. This project does not include a backup system or online service.

Entropy and Key Generation
Entropy means randomness. In this project, randomness is important because it helps make encryption keys difficult to predict.

The program uses
AESGCM.generate_key(bit_length=256) to create a random 256-bit encryption key. it also generates a random 12-byte nonce using os.urandom(12). The nonce helps make each encryption operation unique. 

The same key and nonce are used to decrypt the message during that run of the program. The key is not saved, so the encrypted message cannot be decrypted after the program ends.

How to Run the Program
1.-Install Python 3.
2.-Install the cryptography library using python3 -m pip install cryptography.
3.- Open the project folder in VS Code. 
4.- Open the terminal and run python3 main.py
5.- Enter a message, such as Hello World.
6.- Review the original message, SHA-256
hash, encrypted message, decrypted message, and integrity verification result.

This project helped me understand how hashing and encryption work together to protect information. I learned that SHA-256 can help detect changes to a message, while AES encryption helps keep the information private. I also learned why random keys are important when protecting data.