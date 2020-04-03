#função recebe um inteiro x e verifica quantos primos tem entre 2 e n

def isPrimo(n):
    isPrimo = True
    i=1
    if n== 2:
        return isPrimo
    else:

        while i!=n:
            if i>1 and n % i == 0:
                isPrimo = False
            i = i + 1
        return isPrimo

def n_primos(x):
    count = 0
    i = x
    while i >= 2:
        if isPrimo(i):
            count = count + 1
        i = i - 1

    return count

print(n_primos(2))
print(n_primos(3))
print(n_primos(6))