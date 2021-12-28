"""
In my notes I have listed this as x^2 ≡ a (mod n) for consistency. This puzzle 
uses different letters, so that the formula becomes:
    a^2 ≡ x (mod p)
"""

p = 29              # Note that we have a p that is prime!
ints = [14, 6, 11]  # list of x's that are possible quadratic residues

# Since p is a prime, gcd(x,p) = 1 always, so we dont need to check for this.
# We only need to check if a^2 ≡ x (mod p) has a solution:
res = []
for x in range(p):
    if pow(x, 2, p) in ints:
        res.append(x)


print("Flag: ", min(res))
