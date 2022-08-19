import time     ##importar la biblioteca time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n              ##Es lo mismo que decir respuesta = respuesta * n
        n = n - 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)

if __name__ == '__main__':
    n = 10000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f'con {n} iteraciones se demora {round(final - comienzo,5)} el algoritmo factorial tiempo')

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f'con {n} iteraciones se demora {round(final - comienzo,5)} el algoritmo factorial recursivo')