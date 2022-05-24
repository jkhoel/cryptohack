# Source: https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#gcm-mode

import json
from Cryptodome.Cipher import AES
from base64 import b64encode, b64decode

# ENCRYPT SOME DATA
data = b"hello world, this is secret!"

# KEY TO USE WHEN ENCRYPTING
key = b"some16bytekey123"

# CREATE ENCRYPTION CIPHER AND ENCRYPT DATA
cipher = AES.new(key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(data)

# OUTPUT IN A PRETTY WAY BY BUILDING A JSON OBJECT
json_k = ['nonce', 'ciphertext', 'tag']
json_v = [b64encode(x).decode('utf-8')
          for x in [cipher.nonce, ciphertext, tag]]
result = json.dumps(dict(zip(json_k, json_v)))
print(result)


# DECRYPT
try:
    # ASSUMING WE USE THE JSON ABOVE AS INPUT...
    b64 = json.loads(result)
    jv = {k: b64decode(b64[k]) for k in json_k}

    # CREATE A CIPHER AND DECODE
    cipher = AES.new(key, AES.MODE_GCM, nonce=jv['nonce'])
    plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])

    # OUTPUT THE DATA
    print("The message was:")
    print(plaintext)

except (ValueError, KeyError):
    print("Incorrect decryption")
