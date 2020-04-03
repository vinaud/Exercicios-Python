#recebe os lados do retângulo e o desenha, com o interior vazio

x = int(input("digite a largura"))
y = int(input("digite a altura"))
cx = x
cy = y

while cy > 0:
    while cx > 0:
        print("#",end="")
        cx = cx - 1
    print()
    cx = x
    cy = cy -1