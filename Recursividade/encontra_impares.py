# verifica quais os numeros impares em uma lista, de forma recursiva

def encontra_impares(lista):
    lista2 = []

    if len(lista) == 1:
        if not lista[0] % 2 == 0:
            lista2.extend([lista[0]])
        return lista2
    else:
        if not lista[0] % 2 == 0:
            lista2.extend([lista[0]])
        lista2.extend(encontra_impares(lista[1:]))
        return lista2

print(encontra_impares([7,2,1,2,3,4,5,]))