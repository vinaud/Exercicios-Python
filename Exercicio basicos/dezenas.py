#detecta e imprime o valor do digito da dezena de um numero

numero = int(input("Digite um número inteiro: "))

nsemunidade = numero // 10
dezena = nsemunidade % 10

print("O dígito das dezenas é",dezena)
