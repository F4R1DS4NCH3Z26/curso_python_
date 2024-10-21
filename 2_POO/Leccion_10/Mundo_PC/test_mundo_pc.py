
# from Teclado import Teclado
# from Monitor import Monitor
# from Raton import Raton
from Computadora import Computadora,Teclado,Monitor, Raton
from Orden import Orden


if __name__ == '__main__':

    teclado1 = Teclado("Logitech", "USB")
    teclado2 = Teclado("Janus", "USB") 
    monitor1 = Monitor("Hp", "30 pulgadas")
    monitor2 = Monitor("LG", "30 pulgadas")
    raton1 = Raton("Janus", "Tipo C")
    raton2 = Raton("HP", "USB")
    computadora1 = Computadora("Master Gamer 1", monitor1, teclado1, raton1)
    computadora2 = Computadora("Master Gamer 2", monitor2, teclado2, raton2)
    computadora3 = Computadora("Master Gamer 2", monitor2, teclado2, raton2)

    computadoras1 = [computadora1, computadora2]
    orden1 = Orden(computadoras1)
    orden1.agregar_computadora(computadora3)
    print(orden1)
    # print(orden2)

    
