
# In Python, the chr() function can be used to convert an ASCII ordinal number to a character.
# The ord() function does the opposite.
_arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73,
        73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

str = ""

for i in _arr:
    str += chr(i)


print(str)
