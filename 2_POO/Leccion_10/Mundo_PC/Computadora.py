from Teclado import Teclado
from Monitor import Monitor
from Raton import Raton
class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, raton, teclado, monitor):
        Computadora.contador_computadora += 1
        self._id_computadora = Computadora.contador_computadora
        self._nombre = nombre
        self._raton = raton
        self._teclado = teclado
        self._monitor = monitor

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}'''


if __name__ == '__main__':
    teclado1 = Teclado("Logitech", "USB")
    monitor1 = Monitor("Hp", "30 pulgadas")
    raton1 = Raton("Janus", "Tipo C")
    computadora1 = Computadora("Master Gamer", monitor1, teclado1, raton1)
    print(computadora1)

    teclado2 = Teclado("Logitech", "USB")
    monitor2 = Monitor("Hp", "30 pulgadas")
    raton2 = Raton("Janus", "Tipo C")
    computadora1 = Computadora("Master Gamer", monitor1, teclado1, raton1)
    computadora2 = Computadora("Master Gamer 2", monitor1, teclado1, raton1)
    print(computadora1)
    print(computadora2)