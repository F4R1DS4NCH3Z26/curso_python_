from Producto import Producto
from Orden import Orden

producto1 = Producto('Zapatos Nike', 250000)
producto2 = Producto('Zapatos Adidas', 150000)
producto3 = Producto('Medias polo', 150000)
producto4 = Producto('Buso Facol', 150000)
productos1 = [producto1, producto2]
productos2 = [producto1, producto2, producto2]
orden1 = Orden(productos1)
orden2 = Orden(productos2)
orden1.agregar_producto(producto3)
orden2.agregar_producto(producto4)
print(orden1)
print( f'El total de la primera orden es de {orden1.calcular_total()}')
print(orden2)
print( f'El total de la segunda orden es de {orden2.calcular_total()}')
