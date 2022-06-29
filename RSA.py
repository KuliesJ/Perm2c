from primeNGenerator import genPrimoBits, randomBits
from euclides import euclides
from inverso import inverso
from expMod import expMod

def rsaKeyGenerator():
    # Generar numeros primos p y q
    p = genPrimoBits(16)
    q = genPrimoBits(16)
    while p == q:
        q = genPrimoBits(16)
    # Calcular n = p * q
    n = p * q
    # Calcular phi(n)
    phiN = (p - 1) * (q - 1)
    # Generar e, tal que mcd(e, phiN) = 1
    e = randomBits(32)
    while euclides(e, phiN) != 1:
        e = randomBits(32)
    # Hallar d (la inversa de e)
    d = inverso(e, phiN)
    return ([e, n], [d, n])

def rsaCipher(m, k):
    return expMod(m, k[0], k[1])

if __name__ == "__main__":
    (P, S) = rsaKeyGenerator()
    print(P, S)
    m = 12
    c = rsaCipher(m, P)
    print(m, c, rsaCipher(c, S))