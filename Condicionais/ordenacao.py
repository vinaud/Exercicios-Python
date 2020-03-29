# recebe tres numeros inteiros e verifica se foram inseridos em ordem crescente
a = int(input(" insira o primeiro valor: "))
b = int(input(" insira o sgundo valor: "))
c = int(input(" insira o terceiro valor: "))

if a <= b and a <= c and b <= c:
    print("crescente")
else:
    print("não está em ordem crescente")
