from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    # print(objeto)
    # print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


empleado = Empleado("Farid", 3000000)
imprimir_detalles(empleado)

gerente = Gerente("Laura", 20000000, "Barranquilla")
imprimir_detalles(gerente)


