from euclides import euclides
from millerRabin import MillerRabin

def getPrimes(n):
    primes = []
    for i in range(1, n):
        if euclides(i, n) != 1:
            if MillerRabin(i, 500):
                primes.append(i)
                if len(primes) == 2:
                    break
    return primes