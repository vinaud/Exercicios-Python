# função soma_hipotenusa recebe um inteiro n e calcula a soma de todos
#inteiros entre 1 e n que sejam hipotenusa de algum triangulo

def is_hipotenusa(x):
    i = 1
    j = 1
    hipo = False
    while i < x:
        while j < x:
            if x ** 2 == (i ** 2 + j** 2):
                hipo = True
                break
            j = j + 1
        i = i + 1
        j = 1

    return hipo
  

def soma_hipotenusas(n):
    soma = 0
    contador = 1

    while contador <= n:
        if is_hipotenusa(contador):
            soma = soma + contador
        contador = contador + 1

    return soma


print(soma_hipotenusas(6))
print(soma_hipotenusas(15))
print(soma_hipotenusas(20))
print(soma_hipotenusas(27))