"""
Looking at Fermat's little theorem (https://en.wikipedia.org/wiki/Fermat%27s_little_theorem):

if p is prime, for every integer a:
        pow(a, p) = a mod p

And, if p is prime and a is an integer coprime with p:
        pow(a, p-1) = 1 mod p

So lets check
        pow(273246787654, 65536) mod 65537

Notice that 65536 is exactly 65537-1, and if 273246787654 and 65537 
are coprime then the result is one:
"""
from math import gcd

a = 273246787654
p = 65537

# If a and p are indeed coprime, we expect the result to be 1
if gcd(a, p) == 1:
    print("1 - a and p are coprime!")


# We can verify this:

# Calculates x^y under modulo m
def power(x, y, m):
    if(y == 0):
        return 1
    p = power(x, y // 2, m) % m
    p = (p * p) % m
    return p if (y % 2 == 0) else (x * p) % m


print("Result: " + str(power(273246787654, 65536, 65537)))
