# procura um elemento em uma lista e retorna o índice caso seja encontrado. Retorna falso caso não esteja na lista
def busca(lista, elemento):
    for i in range(len(lista)):
        if elemento == lista[i]:
            return i

    return False