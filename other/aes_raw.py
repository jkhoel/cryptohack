# Source: https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#gcm-mode

from Cryptodome.Cipher import AES
from base64 import b64encode

# ENCRYPT SOME DATA
data = b"hello world, this is secret!"

# KEY TO USE WHEN ENCRYPTING
key = b"some16bytekey123"

# CREATE ENCRYPTION CIPHER AND ENCRYPT DATA
cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(data)
nonce = cipher.nonce

# OUTPUT IN A PRETTY WAY BY BUILDING A JSON OBJECT
print("Nonce:\t\t", b64encode(nonce).decode('utf-8'))
print("Tag:\t\t", b64encode(tag).decode('utf-8'))
print("Ciphertext:\t", b64encode(ciphertext).decode('utf-8'))


# DECRYPT
try:
    # CREATE A CIPHER AND DECODE
    cipher = AES.new(key, AES.MODE_GCM, nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # OUTPUT THE DATA
    print("\nThe message was:")
    print(plaintext.decode('utf-8'))

except (ValueError, KeyError):
    print("Incorrect decryption")
