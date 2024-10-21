from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print("Creacion objeto cuadrado".center(50,"-"))
cuadrado1 = Cuadrado(50, 'Verde')
cuadrado1.ancho = 12
print(f"El ancho es {cuadrado1.ancho}")
print(f"El alto es {cuadrado1.alto}")
print(f"El resultado de el cuadrado es {cuadrado1.calcular_area()}")
print(f"{cuadrado1}")

print("Creacion objeto rectangulo".center(50,"-"))

rectangulo1 = Rectangulo(5, 9, "Rojo")
rectangulo1.ancho = 45
print(f"El resultado del rectangulo  es {rectangulo1.calcular_area()}")
