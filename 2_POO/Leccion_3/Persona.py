class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Mi nombre es {self.nombre} {self.apellido}"

class Empleado(Persona):

    def __init__(self, nombre, apellido, sueldo):
        super().__init__(nombre, apellido)
        self.sueldo = sueldo

    def __str__(self):
        return f'{super().__str__()} Sueldo: {self.sueldo}'

# empleado1 = Empleado("Farid", "Sanchez", 5000)
# print(empleado1.nombre)
    