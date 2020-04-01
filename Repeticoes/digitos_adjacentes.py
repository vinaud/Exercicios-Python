#verifica se um numero tem dois digitos adjacentes iguais

n = int(input("Insira um numero natural"))

n2 = n
digito1 = 0
digito2 = 0

igual = False

while n2 != 0:
    digito1 = n2 % 10
    n2 = n2 // 10
    digito2 = n2 % 10
    if digito1 == digito2:
        igual  = True

if igual:
    print("sim")
else:
    print("não")


