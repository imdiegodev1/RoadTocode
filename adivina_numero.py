import random
def run():
    numero_aleatorio = random.randint(1, 101)
    numero_elejido = int(input('Elije un numero del 1 al 100: '))

    while numero_elejido != numero_aleatorio:
        if numero_elejido < numero_aleatorio:
            print ('Busca un numero màs grande!')
        else:
            print('Busca un numero màs pequeño!')
        numero_elejido = int(input('Elñige otro numero: '))
    print('Lo adivinaste!')

if __name__ == '__main__':
    run()