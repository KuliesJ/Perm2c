from primeNGenerator import genPrimoBits, randomBits
from euclides import euclides
from inverso import inverso
from expMod import expMod

def rsaKeyGenerator(b=32):
    # Generar numeros primos p y q
    p = genPrimoBits(b // 2)
    q = genPrimoBits(b // 2)
    while p == q:
        q = genPrimoBits(b // 2)
    # Calcular n = p * q
    n = p * q
    # Calcular phi(n)
    phiN = (p - 1) * (q - 1)
    # Generar e, tal que mcd(e, phiN) = 1
    e = randomBits(b)
    while euclides(e, phiN) != 1:
        e = randomBits(b)
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