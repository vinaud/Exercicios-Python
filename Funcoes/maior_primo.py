def ePrimo(n):
    isPrimo = True
    i=1

    while i!=n:
       if i>1 and n % i == 0:
           isPrimo = False
       i = i + 1

    return isPrimo

def maior_primo(n):
    while n > 0:
        if ePrimo(n):
            return n
        n = n-1


    

