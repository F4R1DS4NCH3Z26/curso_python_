class MiClase:
    
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
    @staticmethod
    def metodo_estatico():
        print("Hola mundooooooooooooooooo")

    @classmethod
    def metodo_de_clase(cls):
        print(cls.variable_clase)
    
    def metodo_intancia(self):
        self.metodo_estatico()
        self.metodo_de_clase()

MiClase.metodo_estatico()  
MiClase.metodo_de_clase()   
miObjeto1 = MiClase('variable_instancia')
miObjeto1.metodo_de_clase()   
miObjeto1.metodo_intancia()

# print(MiClase.variable_clase)
# miClase = MiClase("Valor variable instancia")
# print(miClase.variable_instancia)
# print(miClase.variable_clase)

# MiClase.variable_clase2 = 'Valor 2 variable de clase'

