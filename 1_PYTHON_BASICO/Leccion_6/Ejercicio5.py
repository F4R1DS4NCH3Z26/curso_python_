def fahrenheit_celsius(fahrenheit):
    resp = (fahrenheit-32) * 5/9
    return resp

fahrenheit = float(input("Valor de fahrenheit: "))

celsius = fahrenheit_celsius(fahrenheit)

print(f"Valor de celsius a fahrenheit: {celsius}")
