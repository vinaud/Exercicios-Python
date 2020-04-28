#exercicio que adiciona o metodo que define o tipo de triangulo foi instanciado, na classe Triangulo
class Triangulo:
    
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return "equilátero"
        elif not self.a == self.b and not self.a  == self.c and not self.b == self.c:
            return "escaleno"
        else:
            return "isóceles"


def main():
    t = Triangulo(1,2,3)
    u = Triangulo(3,3,3)
    v = Triangulo(2,3,3)

    print (t.tipo_lado())
    print (u.tipo_lado())
    print (v.tipo_lado())


main()
