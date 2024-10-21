class Aritmetica:

    """
    Clase que sirve para sacar operaciones aritmeticas
    """
    def __init__(self, operadar1, operadar2):
        self.operador1 = operadar1
        self.operador2 = operadar2

    def sumar(self):
        return self.operador1 + self.operador2


    def restar(self):
        return self.operador1 - self.operador2   

    def multi(self):
        return self.operador1 * self.operador2

    def divi(self):
        return self.operador1 / self.operador2

    def resi(self):
        return self.operador1 % self.operador2

print("")
aritmetica = Aritmetica(4,3)
print(f"La suma de los dos operadores es de {aritmetica.sumar()}")

print("")
print(f"La resta de los dos operadores es de {aritmetica.restar()}")

print("")
print(f"La multiplicacion de los dos operadores es de {aritmetica.multi()}")

print("")
print(f"La division de los dos operadores es de {aritmetica.divi():.2f}")

print("")
print(f"El residuo de los dos operadores es de {aritmetica.resi()}")