def run():
    # nombre = input('Escribe tu nombre: ')      ##Segmento para recorrer un string e imprimir letra por letra
    # for letra in nombre:
    #     print(letra)

    frase = input('Escribe una frase: ')
    for caracter in frase:
        print(caracter.upper())


if __name__ == '__main__':
    run()