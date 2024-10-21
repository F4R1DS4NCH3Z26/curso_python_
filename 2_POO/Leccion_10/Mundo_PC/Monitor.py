class Monitor:
    contador_monitor = 0
    
    def __init__(self, marca, tamaño):
        Monitor.contador_monitor += 1
        self._id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamaño = tamaño

    @property
    def marca(self):
        return self._marca

    @property
    def tamaño(self):
        return self._tamaño
        
    
    def __str__(self):
        return f"Id Monitor: {self._id_monitor}, marca: {self._marca}, tamaño: {self._tamaño}"


if __name__ == '__main__':
    monitor1 = Monitor("Hp", "30 pulgadas")
    print(monitor1)
    
    monitor2 = Monitor("LG", "45 pulgadas")
    print(monitor2)