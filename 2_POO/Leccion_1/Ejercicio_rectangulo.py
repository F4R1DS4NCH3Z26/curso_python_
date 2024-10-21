class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        

    def Area (self):
        return self.base * self.altura

base = float(input("Por favor digite la base: "))
altura = float(input("Por favor digite la altura: "))

rectangulo = Rectangulo(base, altura)

print(f"A = B * H: {rectangulo.Area()}")


