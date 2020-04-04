def remove_repetidos(lista):
    lista2 =[]
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    lista2.sort()
            
    return lista2

print(remove_repetidos([7,3,33,12,3,3,3,7,12,100]))