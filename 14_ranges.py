my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)

my_range2 = range (0, 7, 2)
my_range3 = range (0, 8, 2)

my_range == my_range2         ##puedo modificar el primer rango pero apuntando a otro lado

for i in my_range:
    print (i)

print(id(my_range))
print(id(my_range2))

for i in range (0, 101, 2):    ##genero todos los numeros pares del 0 al 100 de forma ordenada
    print(f'pares {i}')

for i in range (1, 100, 2):    ##Reto platzi de generar todos los impares
    print(f'nones {i}')