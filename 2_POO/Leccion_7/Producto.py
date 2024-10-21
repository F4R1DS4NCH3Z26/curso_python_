class Producto:
    contador_producto = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_producto += 1
        return cls.contador_producto

    def __init__(self, nombre, precio):
        self._id_producto = Producto.generar_siguiente_valor()
        self._nombre = nombre
        self._precio = precio

    @property
    def precio(self):
        return self._precio

    def __str__(self):
        return f'ID Producto: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Zapatos Nike', 250000)
    producto2 = Producto('Zapatos Adidas', 150000)
    print(producto1)
    print(producto2)