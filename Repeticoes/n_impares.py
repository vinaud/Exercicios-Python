#imprime os n primeiros numeros impares na  tela   

n = int(input("insira o valor de n"))
i = 0
impares = 0

while impares != n:
    if i % 2 != 0:
        print(i)
        impares = impares + 1
    i = i + 1
    

