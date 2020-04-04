i = -1
lista = []

while i!=0:
    i = int(input("Digite um número"))
    if i !=0:

        lista.append(i)

lista2 = lista[: : -1]

for item in lista2:
    print(item)



