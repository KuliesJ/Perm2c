# Perm2c

# Integrantes:
- Mariana Cáceres Urquizo
- Camila Orihuela Flores
- Jorge Núñez Paucar

# Instrucciones de ejecución
*Clonar*
```
git clone https://github.com/KuliesJ/Perm2c.git
```
*Ejecutar*
```
python3 ej1.py
python3 ej2.py
python3 ej3.py
```
# [Ejercicio 1](ej1.py)
Para hallar el mensaje "m" primero encontraremos cúales son los números primos "p" y "q" que multiplicados dan n
En este caso específico, es posible dado que el número no es muy grande. Podemos entonces hallar phi(n) con estos dos números "p, q"
Hallando phi(n) podemos hallar la llave secreta y descifrar c

# [Ejercicio 2](ej2.py)
Podemos hacer un ataque de módulo común ya que tenemos un mensaje cifrado dos veces con diferentes exponentes pero mismo módulo
Hallaremos los valores x , y mediante el algoritmo Extendido de Euclides, ya que los necesitamos:
Como e_1 * x + e_2 * y = 1 --> c1^x * c2^y mod n = m --> (x es menor que 0) --> c1_inversa^x * c2^y mod n

# [Ejercicio 3](ej3.py)
Firma digital
