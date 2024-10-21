print("Poporcionar la informacion del un libro")

nombre = input("Ingrese el nombre de el libro, por favor: ")
Id = int(input("Ingrese el id de el libro, por favor: "))
precio = float(input("Ingrese el precio del libro, por favor: "))
envio = input("¿Su envio ser gratis? (True/False) ")
print("")
print("")

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:      
    envio = "Digite un valor valido en el campo envios"
print(f'''Informacion de libro
Nombre: {nombre}
Id Libro: {Id}
Precio: {precio}  
Envio: {envio}''')

    
    
