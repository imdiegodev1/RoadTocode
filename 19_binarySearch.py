import random
import time

def busqueda_binaria (lista, comienzo, final, objetivo, iteraciones = 0):
    
    iteraciones += 1

    if comienzo > final:
        return (False, iteraciones)
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, iteraciones)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iteraciones = iteraciones)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iteraciones = iteraciones)

if __name__ == '__main__':
    
    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    start = time.time()
    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    (encontrado, iteraciones) = busqueda_binaria(lista, 0, len(lista), objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    end = time.time()
    print(f'este algoritmo busqueda binaria toma un tiempo de ejecucion de {round(end - start, 3)}')
    print (f'el numero de iteraciones realizadas en la busqueda fue de {iteraciones}')