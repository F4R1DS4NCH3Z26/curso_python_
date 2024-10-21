cal = float(input("Proporciona un valor del 9 - 10: "))

if 9 < cal <= 10:
    calificacion = "A"
elif 8 < cal <= 9:
    calificacion = "B"
elif 7 < cal <= 8:
    calificacion = "C"
elif 6 < cal <= 7:
    calificacion = "D"
elif 0 < cal <= 7:
    calificacion = "F"
else: 
    calificacion = "VALOR DESCONOCIDOS"
print("")
print("-------------------------------------")
print(f"Su calificacion es: {calificacion}               -")
print("-------------------------------------")




