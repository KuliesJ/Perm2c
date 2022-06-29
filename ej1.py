from RSA import rsaCipher
from inverso import inverso
from getPrimes import getPrimes

P = [65537, 999630013489]
c = 747120213790

if __name__ == "__main__":
    primes = getPrimes(P[1])

    phiN = (primes[0] - 1) * (primes[1] - 1)
    S = [inverso(P[0], phiN), P[1]]

    m = rsaCipher(c, S)
    c2 = rsaCipher(m, P)
    print("m =", m, "\nc = ", c2, "\nP(m) = c?:",  c == c2)