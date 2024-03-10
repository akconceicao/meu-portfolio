class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def calcular_area(self):
        return self.lado_a * self.lado_b


retangulo = Retangulo(4, 6)
area = retangulo.calcular_area()
print("A área do retângulo é:", area)
