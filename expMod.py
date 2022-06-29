"""
def expMod(a, x, n):
    if x == 0:
        return 1
    elif x % 2 == 0:
        t = expMod(a, x / 2, n)
        return (t * t) % n
    else:
        t = expMod(a, x - 1, n)
        return (t * (a % n)) % n
"""

def expMod(a, x, n):
    c = a % n
    r = 1
    while x > 0:
        if x % 2 == 1:
            r = (r * c) % n
        c = (c * c) % n
        x = x // 2
    return r

def expModBits(x, y, z):
    c = 0
    d = 1
    n = y.bit_length()
    for i in range(n):
        c = 2 * c
        d = (d * d) % z
        if y & 2 ** (n - 1):
            c += 1
            d = (d * x) % z
        y = y << 1
    return d
