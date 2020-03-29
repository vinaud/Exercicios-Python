#Analiza se um número é divisivel por 3 e 5

numero = int(input("Insira um número para verificar se é divisivel por 3: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")

else:
    print(numero)
