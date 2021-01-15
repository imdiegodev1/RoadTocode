import random
import time

def ordenamiento_por_insercion (lista):
    for indice in range (1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    return lista

if __name__ == '__main__':

    tamano_de_lista = int(input('De que tamaño sera la lista? '))
    start = time.time()
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    lista_ordenada = (ordenamiento_por_insercion(lista))
    print(lista)
    end = time.time()
    print(f'este algoritmo de ordenaciòn toma un tiempo de ejecucion de {round(end - start, 3)}')