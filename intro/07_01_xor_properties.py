""" 
https://cryptohack.org/courses/intro/xor1/

There are four main properties we should consider when we solve challenges using the XOR operator:
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

Let's break this down:
Commutative means that the order of the XOR operations is not important. 
Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). 
The identity is 0, so XOR with 0 "does nothing"
Self-Inverse: something XOR'd with itself returns zero.
"""

# Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties
# to undo the encryption in the final line to obtain the flag.

# !!! Before you XOR these objects, be sure to decode from hex to bytes !!!

# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf


def bxor(b1, b2):
    # It seems we cannot XOR bytes in Python (?), so we need to create a function to do that
    result = bytearray(b1)
    for i, b in enumerate(b2):
        result[i] ^= b
    return bytes(result)


def findKeyByXORproduct(k1, k1XORk2):
    # We use the Associative property to find one of the keys of a XOR product
    k = bxor(k1, k1XORk2)
    print("Check for Key:", bytes.hex(bxor(k1, k)))
    return k

    # Convert the known key to bytes
_key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")

# Convert the known XOR products to bytes
_product_key1_xor_key2 = bytes.fromhex(
    "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
_product_key2_xor_key3 = bytes.fromhex(
    "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")

_product_flag_xor_all_keys = bytes.fromhex(
    "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# Use the Associative property to find keys 2 and 3, since we know what KEY2 ^ KEY1 and KEY2 ^ KEY3 should become:
_key2 = findKeyByXORproduct(_key1, _product_key1_xor_key2)
_key3 = findKeyByXORproduct(_key2, _product_key2_xor_key3)

# We know that order of operations are not important (Commutative property) and we know we can exploit the Associative property to find _key1 ^ _key2 ^ _key3
_key123 = bxor(_key1, _product_key2_xor_key3)

# Find the flag now by using the Associative property one last time
_flag_as_bytestring = findKeyByXORproduct(_key123, _product_flag_xor_all_keys)

print("FLAG: " + _flag_as_bytestring.decode("utf-8"))
