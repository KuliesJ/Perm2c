from hashlib import sha1
from RSA import rsaKeyGenerator, rsaCipher

if __name__ == "__main__":
    (P, S) = rsaKeyGenerator(162)
    M = b"HelloWorld"
    h = sha1()
    h.update(M)
    m = int(h.hexdigest(), 16)
    print(h.hexdigest())

    # Firma digital
    sigma = rsaCipher(m, S)

    u = rsaCipher(sigma, P)

    print(M, m, sigma, u, u == m)
