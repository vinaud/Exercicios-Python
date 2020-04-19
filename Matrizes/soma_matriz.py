# recebe duas matrizes e faz a soma delas caso suas dimensões sejam iguais

def soma_matrizes(m1,m2):
    soma =[]
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range(len(m1)):
            soma.append([])
            for j in range(len(m1[0])):
                valor = m1[i][j] + m2[i][j]
                soma[i].append(valor)
        return soma

    return False
