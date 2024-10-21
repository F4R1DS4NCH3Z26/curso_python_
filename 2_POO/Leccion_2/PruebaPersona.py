from Metodo_get_y_set import Persona 


print("Creacion de objetos".center(30,"-"))
persona1 = Persona("Juan", "Hernandez", 15)
persona1.mostrarDetalles()
print(__name__)

print("Eliminación de objetos".center(30,"-"))

del persona1
