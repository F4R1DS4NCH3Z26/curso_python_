def multiplicar(*numeros):
    multi = 1
    for numero in numeros:
        multi *= numero

    return multi 

print(multiplicar(1,2,3))



