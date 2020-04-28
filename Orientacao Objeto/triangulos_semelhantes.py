class Triangulo:
    
    def __init__(self, lado_a, lado_b, lado_c):
        self.a = lado_a
        self.b = lado_b
        self.c = lado_c

    def get_lados_ordenados(self):
        lados = [self.a, self.b, self.c]
        lados.sort()
        return lados

    def perimetro(self):
        return self.a + self.b + self.c
    
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return "equilátero"
        elif not self.a == self.b and not self.a  == self.c and not self.b == self.c:
            return "escaleno"
        else:
            return "isóceles"
    
    def maior_lado(self):
        if self.a > self.b and self.a> self.c:
            return "a"
        elif self.b >self.c and self.b > self.a:
            return "b"
        else:
            return "c"


    def retangulo(self):
        hipotenusa = self.maior_lado()
        if hipotenusa == "a":
            if self.a ** 2 ==  self.b ** 2 + self.c **2:
                return True
            else:
                return False
        elif hipotenusa == "b":
            if self.b ** 2 ==  self.a ** 2 + self.c **2:
                return True
            else:
                return False

        elif hipotenusa == "c":
            if self.c ** 2 ==  self.a ** 2 + self.b **2:
                return True
            else:
                return False

    def semelhantes(self, triangulo):
        lados_self = self.get_lados_ordenados()
        lados_t2 = triangulo.get_lados_ordenados()
        for i in range(len(lados_self)):
            
            if lados_self[i] > lados_t2[i] :
                if not lados_self[i] % lados_t2[i] == 0:
                    return False
            else:
                if not lados_t2[i] % lados_self[i] == 0:
                    return False

        return True


def main():
    t = Triangulo(1,2,3)
    u = Triangulo(3,3,3)
    v = Triangulo(2,3,3)
    w = Triangulo(3,4,5)
    x = Triangulo(6,6,6)
    w2 = Triangulo(6,8,10)

    
    print(w.semelhantes(w2))
    print(u.semelhantes(x))
    print(w.semelhantes(t))

main()