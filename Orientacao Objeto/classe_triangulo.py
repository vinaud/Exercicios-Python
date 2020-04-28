class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def perimetro(self):
        return self.a + self.b + self.c

def main():
    t = Triangulo(1,2,3)
    print(t.perimetro())


main()
