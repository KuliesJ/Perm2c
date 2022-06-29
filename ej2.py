from expMod import expMod
from euclides import euclides, euclidesExt
from millerRabin import MillerRabin
from RSA import rsaCipher

P = [7, 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667]
P_prima = P.copy()
P_prima[0] = 11
c = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
c_prima = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184

if __name__ == "__main__":
    #Ejercicio 2
    (z, x, y) = euclidesExt(P[0], P_prima[0])
    var = expMod(c, x, P[1])
    var2 = expMod(c_prima, y, P[1])
    res = (var * var2) % P[1]
    res = res % P[1]
    print(res, rsaCipher(res, P))
