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

       

def main():
    t = Triangulo(1,2,3)
    u = Triangulo(3,3,3)
    v = Triangulo(2,3,3)
    w = Triangulo(3,4,5)

    print(t.retangulo())
    print(u.retangulo())
    print(v.retangulo())
    print(w.retangulo())


main()