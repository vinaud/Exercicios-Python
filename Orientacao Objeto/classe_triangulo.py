class Triangulo:

    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

def main():
    t = Triangulo(1,2,3)
    print(t.perimetro())


main()
