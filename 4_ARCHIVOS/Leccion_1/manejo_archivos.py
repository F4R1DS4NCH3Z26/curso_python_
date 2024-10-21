try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos un archivo txt\n')
    archivo.write('I am the dick')
    archivo.write('Transformación')
except Exception as e: 
    print(e)
finally:
    archivo.close() 