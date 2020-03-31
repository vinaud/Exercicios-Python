#imprime os n primeiros numeros impares na  tela   

n = int(input("insira o valor de n"))
i = 0

while i <= n:
    if i % 2 != 0:
        print(i)
    i = i + 1
    

