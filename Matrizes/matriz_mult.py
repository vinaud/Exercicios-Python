# função que recebe duas matrizes e verifica se são multiplicaveis entre si

def sao_multiplicaveis(m1, m2):
    if len(m1[0]) == len(m2): 
        return True
    else:
        return False
