def numerosDesc(numero):
    if numero >= 1:
        print(numero)
        numerosDesc(numero-1)
        

print(numerosDesc(5))