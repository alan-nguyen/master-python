def gcd(a, b):
    # Find the greatest common denominator of two number
    # using Euclid's algorithm
    while (b != 0):
        t = a
        a = b
        b = t % b
    return a

# test case
print(gcd(60, 96))
print(gcd(20, 8))