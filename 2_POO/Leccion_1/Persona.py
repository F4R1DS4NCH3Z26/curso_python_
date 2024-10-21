class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrarDetalles (self):
        print(f"Mi nombre es {self._nombre} {self.apellido}")


persona1 = Persona("Farid", "Sanchez", 21, "1234567890",1,2,3,4, m = "manzana", b = "balon")
# persona1.mostrarDetalles()
# print(f"Mi nombre es {persona1.nombre} {persona1.apellido} y tengo {persona1.edad} años. Valores: {persona1.valores}, Terminos: {persona1.terminos} ")


persona1._nombre = "Carlos Andres"
# persona1.apellido = "Orozco Angulo"
# persona1.edad = 26
persona1.mostrarDetalles()

# print(f"Mi nombre es {persona1.nombre} {persona1.apellido} y tengo {persona1.edad} años")

# persona2 = Persona("Juan", "Sanchez", 22)
# print(f"Mi nombre es {persona2.nombre} {persona2.apellido} y tengo {persona2.edad} años")
