#soma os digitos do valor inserido
n = int(input(" insira um número para a soma de seus digitos: "))
n2 = n
finalN = 0

while n2>0:
    finalN = finalN + n2 % 10
    n2 = n2 // 10

print(finalN)

