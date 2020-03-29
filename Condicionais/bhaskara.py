#programa para resolver equação de segundo grau ( raizes reais apenas)

import math

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

delta = b ** 2 - 4 * a * c
if delta == 0:
    resultado = (-b /(2 * a))
    print("a raiz desta equação é",resultado)

elif delta > 0:
    raizDelta = math.sqrt(delta)

    resultado1= (-b + raizDelta)/(2 * a)
    resultado2= (-b - raizDelta)/(2 * a)

    if resultado1 <= resultado2:
        print("as raízes da equação são",resultado1,"e",resultado2)
    else:
        print("as raízes da equação são",resultado2,"e",resultado1)
    


else:
    print("esta equação não possui raízes reais")



        
