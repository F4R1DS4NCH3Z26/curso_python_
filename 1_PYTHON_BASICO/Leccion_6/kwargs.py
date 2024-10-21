def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(ASOCAHO = 'Asociacion de achones de Colombia')
