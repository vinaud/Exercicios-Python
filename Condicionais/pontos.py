import math

#calcula a distancia entre dois pontos num plano cartesiano

x1 = int(input("Insira a coordenada x do ponto 1"))
y1 = int(input("Insira a coordenada y do ponto 1"))

x2 = int(input("Insira a coordenada x do ponto 2"))
y2 = int(input("Insira a coordenada y do ponto 2"))

dxy = math.sqrt((x1 - x2) ** 2 + (y1 - y2) **2)

if dxy >= 10:
    print("longe")

else:
    print("perto")
    

