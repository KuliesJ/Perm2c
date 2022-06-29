
from euclides import euclides, euclidesExt
from expMod import expMod
from euclides import euclides, euclidesExt
from millerRabin import MillerRabin

if __name__ == "__main__":
    #Ejercicio 1
    Primes = []
    for i in range(1,999630013489):
        if(euclides(i, 999630013489)!=1):
            if(MillerRabin(i, 500)):
                Primes.append(i)
                if len(Primes)==2:
                    break
    print(Primes)
    
    #Ejercicio 2
    P =[7, 11, 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667]
    c =35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
    c_prima =35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184
    (z, x, y) = euclidesExt(P[0], P[1])
    var = expMod(c, x, P[2])
    var2 = expMod(c_prima, y, P[2])
    res = var * var2
    res = res%P[2]
    print(res)
