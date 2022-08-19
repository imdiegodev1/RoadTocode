import random
import time

def busqueda_lineal(lista, objetivo, iteraciones=0):
    match = False

    for elemento in lista:
        iteraciones += 1
        if elemento == objetivo:
            match = True
            break
    return (match, iteraciones)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    start = time.time()
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    (encontrado, iteraciones) = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    end = time.time()
    print(f'este algoritmo busqueda lineal toma un tiempo de ejecucion de {round(end - start, 3)}')
    print (f'el numero de iteraciones realizadas en la busqueda fue de {iteraciones}')