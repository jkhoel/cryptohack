"""
https://cryptohack.org/courses/intro/xorkey0/

For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
"""
from pwn import xor
from re import search

cipher = bytes.fromhex(
    "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

print("Here is your flag:")
# A single bytes means an integer value of between 0-255, assuming it is unsigned
for i in range(256):
    # Lets wrap it in a try-catch as some of the XOR results might not be decodable (non-ascii characters)
    try:
        # Make a candidate to check for flag
        _candidate = xor(cipher, i).decode('utf8')

        # We know that the flag will have a certain format, so we can use that to filter out
        if _candidate.startswith('crypto'):
            print(_candidate)

    except:
        pass
