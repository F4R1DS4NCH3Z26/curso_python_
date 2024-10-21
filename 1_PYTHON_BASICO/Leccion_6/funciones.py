# def mi_funcion_python(nombre = 'Lucho', apellido = 'Torres'):
#     return f"Mi nombre es {nombre} {apellido}"

# respuesta = mi_funcion_python('Farid', 'Sanchez')

# # print(respuesta)
# def sumar(a = 0, b = 0) -> int:
#     return a + b

# resultado = sumar()
# print(f'Resultado de la suma es {resultado}')
# print(f'Resultado de la suma es {sumar(10,7)}')


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
