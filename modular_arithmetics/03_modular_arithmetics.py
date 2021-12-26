"""
The Congruence modulo relatuon can be transformed to a modulo operation:
a ≡ b mod m <=> a % m = b

Since a ≡ b mod m, then if we divide the integer a by m we get the remainder is b . b is then the remainder of the euclidean division between a and m.
"""
x = 11 % 6                  # 11 ≡ x mod 6
y = 8146798528947 % 17      # 18146798528947 ≡ y mod 17

print(min(x, y))
