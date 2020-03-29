#programa para resolver equação de segundo grau ( raizes reais apenas)

import math

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

delta = b ** 2 - 4 * a * c
if delta == 0:
    resultado = (-b /(2 * a))
    print("raiz única =", resultado)

elif delta > 0:
    raizDelta = math.sqrt(delta)

    resultado1= (-b + raizDelta)/(2 * a)
    resultado2= (-b - raizDelta)/(2 * a)

    print("x1 =", resultado1)
    print("x2 =", resultado2)

else:
    print("Essa equação não possui raiz no domínio dos Reais")



        
