import hashlib
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Module 4 Midterm - Secure Data Transmission App

message = input("Enter a message: ")

print("Original message:", message)

message_hash = hashlib.sha256(message.encode()).hexdigest()

print("SHA-256 Hash:", message_hash)

key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

nonce = os.urandom(12)

encrypted_message = aesgcm.encrypt(
    nonce, message.encode(), None
)

print("Encrypted message:", encrypted_message.hex())

decrypted_message = aesgcm.decrypt(
    nonce, encrypted_message, None
).decode()

print("Decrypted message:", decrypted_message)

decrypted_hash = hashlib.sha256(
    decrypted_message.encode()
).hexdigest()

if message_hash == decrypted_hash:
    print("Integrity verified: Hashes match!")
else:
    print("Integrity failed: Hashes do not match!")    


