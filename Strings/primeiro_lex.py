# recebe uma lista de strings como parâmetro e devolve o primeiro string na ordem lexicográfica.
def primeiro_lex(lista):
    menor = lista[0]

    for item in lista:
        if item < menor:
            menor = item


    return menor