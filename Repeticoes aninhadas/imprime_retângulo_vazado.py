#recebe os lados do retângulo e o desenha, com o interior vazio

x = int(input("digite a largura"))
y = int(input("digite a altura"))
cx = x
cy = y

while cy > 0:
    while cx > 0:
        if cx == x or cx == 1:
           print("#",end="")
        elif  cy == y or cy == 1:
           print("#",end="")
        else:
            print(" ",end = "")
        cx = cx - 1
    print()
    cx = x
    cy = cy -1
    