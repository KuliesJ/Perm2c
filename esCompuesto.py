from expMod import expMod

def descomponerBase2(n):
    t = 0
    u = n - 1
    while u % 2 == 0:
        u //= 2
        t += 1
    return (t, u)

def esCompuesto(a, n, t, u):
    x = expMod(a, u, n)
    if x == 1 or x == n - 1:
        return False
    for i in range(1, t + 1):
        x = expMod(x, 2, n)
        if x == n - 1:
            return False
    return True
