from Producto import *
from Orden import *

if __name__ == '__main__':
    producto1 = Producto('Zapatos Nike', 250000)
    producto2 = Producto('Zapatos Adidas', 150000)
    producto3 = Producto('Blusa Mattlesa', 34000)
    producto4 = Producto('Tacones', 54500)

    productos1 = [producto1, producto2]
    productos2 = [producto3, producto4]

    orden1 = Orden(productos1)
    print(orden1)
    orden1.agregar_producto(producto3)
    print(f'El total a pagar es de: {orden1.calcular_total()}')

    orden2 = Orden(productos2)
    print(orden2) 
    print(f'El total a pagar es de: {orden2.calcular_total()}')

 
