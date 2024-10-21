archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read(5))
# print(archivo.read(3))

# for linea in archivo:
#     print(linea)0

# print(archivo.readlines()[0])

#  abrimos un nuevo archivo 
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()