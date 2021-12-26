# Greates Common Divisor using Euclid's Algorithm

# Get input values
# input = [12, 8]
input = [66528, 52920]

# Sort them in descending order of magnitude
input.sort(reverse=True)

# Get the values into variables that are more litteral
a = input[0]
b = input[1]

# The GCD will be the value of a and b when the remainder is zero. We will call gcd() recursivly until that happens


def gcd(a, b):
    if(b == 0):
        return a
    return gcd(b, a % b)


print("GCD:", gcd(a, b))

# Alternate solution using conditional (ternary) expressions.


def gcd(a, b): return gcd(b % a, a) if a else b


print("GCD: ", gcd(66528, 52920))
