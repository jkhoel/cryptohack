"""
Looking again at Fermat's little theorem:

if p is prime, for every integer a:
        pow(a, p) = a mod p
and, if p is prime and a is an integer coprime with p:
        pow(a, p-1) = 1 mod p

We can do some magic like this (a^b means pow(a,b)):
        a^(p-1) = 1 (mod p)
        a^(p-1) * a^-1 = a^-1 (mod p)
        a^(p-2) * a * a^-1 = a^-1 (mod p)
        a^(p-2) * 1 = a^-1 (mod p)

So finally we have:
        a^(p-2) = a^-1 (mod p)

So, doing a^(p-2) and then (mod p) we can achieve our result
"""
from Crypto.Util.number import inverse
from math import gcd, pow

# Finds modular inverse of a under modulo m, assuming m is prime


def mod_inverse(a, m):
    if(gcd(a, m) != 1):
        print("Inverse does not exist!")
    else:
        # if a and m are relatively prime, then mod inverse is a^(m-2) mod m
        print("Modular multiplicative inverse is ", pow(a, m - 2) % m)


mod_inverse(3, 13)

"""
Another way to look at it is like this:

The problem given is 3 * d ≡ 1 mod 13

To calculate d we can divide both sides by 3 which gives us:
  d = (1/3) * 1 mod 13 

And we can rewrite that to:
  d = 3^-1 mod 13

This is what the hint about the theorem eludes to as this is basically the inverse of 3 mod 13.
"""
a = 3
p = 13

print(pow(a, p - 2) % p)

"""
Or - just cheat and use some library ;)
"""
print(inverse(3, 13))
