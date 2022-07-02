from cmath import exp
from expMod import expMod, expModBits
from euclides import euclides, euclidesExt
from millerRabin import MillerRabin
from RSA import rsaCipher
from inverso import inverso
P = [7, 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667]
P_prima = P.copy()
P_prima[0] = 11
c = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
c_prima = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184

if __name__ == "__main__":
    #Ejercicio 2
    if (euclides(P[0], P_prima[0]==1) and euclides(c_prima, P[1])):
        print("Es posible un ataque por modulo comun")
        (z, x, y) = euclidesExt(P[0], P_prima[0])
        print("x:", x, "\ny:", y)
        var = 0
        var2 = 0
        if x < 0:
            var = expMod(inverso(c, P[1]), -x, P[1])
        else:
            var = expMod(c, x, P[1])
        if y < 0:
            var2 = expModBits(inverso(c_prima, P[1]), -y, P[1])
        else:
            var2 = expModBits(c_prima, y, P[1])
        m = (var * var2) % P[1]
        shouldBeC = rsaCipher(m, P)
        print(m, shouldBeC, c)
        print(shouldBeC == c)
        #y>0
        #Sacar inversa a c en modulo n
        #Debo resolver inversa(c, n) ^x * c_prima^y mod n
    else:
        print(":c")
