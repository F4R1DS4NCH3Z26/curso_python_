
def calcular_total(pagos, impuesto):
    pag = pagos + ((pagos*impuesto)/100)
    return pag

 
pagos = float(input("Proporciona el valor: "))

impuesto = float(input("Proporciona el impuesto: "))

total = calcular_total(pagos, impuesto)

print(f"El valor con el impuesto agregado es de: {total}")