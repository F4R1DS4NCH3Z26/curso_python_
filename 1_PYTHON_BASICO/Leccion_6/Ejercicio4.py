def celsius_fahrenheit(celsius):
    resp = (celsius * 9/5) + 32
    return resp

celsius = float(input("Valor de celsius: "))

fahrenheit = celsius_fahrenheit(celsius)

print(f"Valor de celsius a fahrenheit: {fahrenheit}")

