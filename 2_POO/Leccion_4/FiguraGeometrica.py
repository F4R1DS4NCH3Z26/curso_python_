#ABC = Abstract Base Class
from abc import ABC, abstractclassmethod, abstractmethod
class FiguraGeometrica(ABC):

    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0


    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0

    @abstractmethod
    def calcular_area(self):
        pass

    def __str__(self):
        return f"FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]"
    
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False