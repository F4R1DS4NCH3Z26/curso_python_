mes = int(input('Proporciona mes del año (1-12): '))

if mes == 1 or mes == 2 or mes == 3:
    print("Es invierno")
elif mes == 4 or mes == 5 or mes == 6:
    print("Es verano")
elif mes == 7 or mes == 8 or mes == 9:
    print("Primavera")
elif mes == 10 or mes == 11 or mes == 12:
    print("Otoño")
else:
    print("NO APLICA")