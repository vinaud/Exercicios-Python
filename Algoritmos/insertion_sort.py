# método de ordenação pelo algoritmo insertion sort
def insertion_sort(lista):
    i = 1
    
    while i < len(lista):
        j = i
        

        while j > 0 and lista[j-1] > lista[j]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            print(j)
            j = j - 1
        i = i + 1
    return lista


print(insertion_sort([4,5,6,3,8,9,2]))

