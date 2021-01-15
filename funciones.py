def enumeracion (objetivo):
    respuesta=0

    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1
    
    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aproximacion (objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo))
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print (f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria (objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo)/2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo= {bajo}, alto = {alto}, respuesta= {respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
    
        respuesta = (alto + bajo)/2

    print(f'La raiz cuadrada de {objetivo} es {respuesta}')

opcion = int(input('Escoja una forma de encontrar la raiz: \n 1. enumeracion. \n 2. aproximacion \n 3. busqueda binaria \n'))

if opcion == 1:
    print ('1. Enumeracion')
    numero = int(input('Escoge un numero: '))
    enumeracion(numero)
elif opcion == 2:
    print ('2. aproximacion')
    numero = int(input('Escoge un numero: '))
    aproximacion(numero)
elif opcion == 3:
    print ('3. busqueda binaria')
    numero = int(input('Escoge un numero: '))
    busqueda_binaria(numero)
else:
    print('No es una opcion valida')
