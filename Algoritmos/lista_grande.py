# dado n, gera uma lista com n inteiros
from random import randint


def lista_grande(n):
    lista = []
    
    for i in range(n):
        x = randint(0,100000)
        lista.append(x)

    return lista

print(lista_grande(5))
print(lista_grande(4))
