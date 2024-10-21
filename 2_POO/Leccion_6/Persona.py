class Persona:

    contador_personas = 0


    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas +=1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.persona_id = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona: [{self.persona_id}], nombre: [{self.nombre}], edad: [{self.edad}]'

persona = Persona('Lucho', 45)
persona2 = Persona('Juan', 25)
persona3 = Persona('Pedro', 45)
print(persona)
print(persona2)
print(persona3)