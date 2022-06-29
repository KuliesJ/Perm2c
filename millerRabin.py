from random import randint
from esCompuesto import esCompuesto, descomponerBase2

def MillerRabin(n, s):
    (t, u) = descomponerBase2(n)
    for i in range(s):
        a = randint(2, n - 1)
        if esCompuesto(a, n, t, u):
            return False
    return True
