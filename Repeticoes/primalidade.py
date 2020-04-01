#verifica se um número é primo

n = int(input("Insira um numero natural"))
isPrimo = True
i=1

while i!=n:
    if i>1 and n % i == 0:
        isPrimo = False
    i = i + 1

if isPrimo:
    print("primo")
else:
    print("não primo")


