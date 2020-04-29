#ordena uma lista usando o selection sort

def ordena(lista):
    for i in range(len(lista)-1):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        
        lista[menor],lista[i] = lista[i], lista[menor]

    return lista


