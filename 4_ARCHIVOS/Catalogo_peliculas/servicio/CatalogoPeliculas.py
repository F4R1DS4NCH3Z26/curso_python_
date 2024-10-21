import os


class CatalogoPeliculas:

    ruta_archivo = 'Peliculas.txt'

    @classmethod
    def agregar_peliculas(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catlogo de Peliculas'.center(50,'-'))

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Se elimino el archivo: {cls.ruta_archivo}')