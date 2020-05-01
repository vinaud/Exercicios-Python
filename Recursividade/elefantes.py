"""
Implemente a função incomodam(n) que devolve uma string contendo "incomodam " 
(a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente positivo, 
a função deve devolver uma string vazia. Essa função deve ser implementada utilizando recursão.

Utilizando a função acima, implemente a função elefantes(n) que devolve uma string contendo 
a letra da música "Um elefante incomoda muita gente" de 1 até n elefantes. Se n não for maior que 1,
 a função deve devolver uma string vazia. Essa função também deve ser implementada utilizando recursão.
"""

def incomodam(n):
    if n < 1:
        return ""
    return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n < 1:
        return ""
    if n == 1:
        return "Um elefante incomoda muita gente\n"
    if n == 2:
        return elefantes(n-1)+str(n)+" elefantes "+incomodam(n)+"muito mais\n" 

    return elefantes(n-1)+str(n-1)+" elefantes incomodam muita gente\n"+str(n)+" elefantes " + incomodam(n)+"muito mais\n" 

print(elefantes(4))