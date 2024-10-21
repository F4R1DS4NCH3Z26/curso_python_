class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f"es de color {self.color} y tiene {self.ruedas} ruedas de repuesto"


class Coche(Vehiculo):

    def __init__(self, color, ruedas,velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    
    def __str__(self):
        return f"{super().__str__()} y corre a {self.velocidad} Km/Hr"


class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} y es de tipo {self.tipo}"


vehiculo1 = Vehiculo("Verde", 2)
print(vehiculo1)

vehiculo1 = Coche("Verde", 2, 45)
print(f"Mi coche {vehiculo1}")

vehiculo1 = Bicicleta("Roja", 1, "Urbana")
print(f"Mi Bicicleta {vehiculo1}")
    
    