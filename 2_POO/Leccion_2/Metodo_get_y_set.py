class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido}")

    def mostrarDetalles (self):
        print(f"Mi nombre es {self._nombre} {self._apellido} y tengo {self._edad} años")

if __name__ == "__main__":
    persona1 = Persona("Farid", "Sanchez", 21)
    persona1.nombre = "Wilfredo Andres"
    persona1.apellido = "Perez Hernandez"
    persona1.edad = 45
    print(persona1.mostrarDetalles())
    print(persona1.nombre)

# print(__name__)

