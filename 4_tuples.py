my_tuple = (1, 'dos', True)

print(type(my_tuple))
print(my_tuple[2])

my_tuple2 = (1,)    ##Es muy importante que si una tupla tiene solo un elemento su definicion tenga este formato

x, y, z = my_tuple   ##Esta es la forma de asignarle una variable a cada valor de la tupla para desempaquetar la tupla

print(x)             ##Aqui llamo los valores desempaquetados de una tupla

def coordenadas():
    return (5, 4)

coordenada = coordenadas()

print (coordenada)

a, b = coordenadas ()
print (a)