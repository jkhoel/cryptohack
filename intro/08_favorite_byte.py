"""
https://cryptohack.org/courses/intro/xorkey0/

For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
"""

cipher = bytes.fromhex(
    "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")


def bxor(b1, b2):
    result = bytearray(b1)
    for i, b in enumerate(b2):
        result[i] ^= b
    return bytes(result)


# A single bytes means an integer value of between 0-255, assuming it is unsigned
for i in range(0, 255):
    print(i)
