# imprime o fatorial de um numero natural

n = int(input("Insira um número natural"))

i = 1 
fatorial = 1

if n == 0:
    fatorial = 0
else:
    while i <= n:
     fatorial = fatorial * i
     i = i + 1

print(fatorial)

