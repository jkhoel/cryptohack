from pwn import xor

"""
I've encrypted the flag with my secret key, you'll never be able to guess it.

Remember the flag format and how it might help you in this challenge!
"""

from pwn import xor

cipher = bytes.fromhex(
    "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

# For this challenge we need to use the associative property; We know some of what the message/flagg will look like
# and this means that the following would be true:
# cipher ^ secret_key = "crypto{...}"   <=> cipher ^ "crypto{...}" = secret_key
#
# However, we can only know the first 7 characters for sure. But we can use this to create a partial key:
partial_key = xor(cipher[:7], "crypto{")

# So now we have our partial key "myXORke" - but with some imaination, and since we could guess the key uses actual words,
# we can guess that the partial_key should actually be:
partial_key = "myXORkey"

# If we assume this is the complete key, 8 chars long - then we probably need to repeat it over the full cipher (42 chars).
# However, 8 times 5 is only 40, so we would need to repeat 6 times to cover everything. Luckily, xor() fixes this problem for us
# and we can just supply it with two asymetrical byte-strings without issue:
flag = xor(cipher, partial_key.encode())

print("Here is your flag:")
print(flag.decode("utf8"))
