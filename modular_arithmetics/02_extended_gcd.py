p = 26513
q = 32321


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, u, v = extended_gcd(b % a, a)
    return gcd, v - (b//a) * u, u


g, u, v = extended_gcd(p, q)
print("au+bv = gdc(a,b) => u,v:", u, v)
print("GCD:", g)
