"""
https://cryptohack.org/courses/intro/xor0/

XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most
challenges and programming languages you will see the caret ^ used instead.

A	B	Output
0	0	0
0	1	1
1	0	1
1	1	0

For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. We can XOR integers by first converting the integer from decimal to binary. We can
XOR strings by first converting each character to the integer representing the Unicode character.

The Python pwntools library has a convenient xor() function that can XOR together data of different types and lengths. But first, you may want to implement your
own function to solve this.
"""

# Given the string "label", XOR each character with the integer 13. Convert these integers back to a string and submit the flag as crypto{new_string}.
_str = "label"
_int = 13

# Declare a string to hold our flag value
new_string = ""

# Convert each character of _str to integer representation of Unicode character, XOR with _int and
# add the result to new_string as a character representation of the product integer
for c in _str:
    # ord() converts a char to an int, and then we do the XOR ^
    res = ord(c) ^ _int
    # chr() converts an in to a char (opposite of ord()) and then we add that to new_string
    new_string += chr(res)

# Print the flag
print("crypto{" + str(new_string) + "}")
