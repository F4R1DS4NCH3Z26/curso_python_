class Cubo:
    
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad


print("")
ancho = float(input("Por favor digite el ancho: "))

print("")
alto = float(input("Por favor digite el alto: "))

print("")
profundidad = float(input("Por favor digite la profundidad: "))

ResultCubo = Cubo(ancho, alto, profundidad)

print("")
print(f"El volumen de el Cubo: {ResultCubo.calcular_volumen()}")
