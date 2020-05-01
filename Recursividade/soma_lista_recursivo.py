# soma os elementos de uma lista de forma recursiva
def soma(lista):
    
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma(lista[1:])

print(soma([1,2,3,4,5,]))
