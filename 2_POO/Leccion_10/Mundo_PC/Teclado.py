from  DispositivosEntrada import DispositivosEntradas
class Teclado(DispositivosEntradas):
    contador_teclado = 0
    
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return f"Id Teclado: {self._id_teclado}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}"


if __name__ == '__main__':
    teclado1 = Teclado("Logitech", "USB")
    print(teclado1)
    teclado2 = Teclado("Logitech", "Blutooth")
    print(teclado2) 