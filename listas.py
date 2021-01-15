my_list = [1,2,3]         ##Definir una lista
print(my_list[0])         ##Llamar un elemento

print(my_list[1:])        ##Llamar una serie de elementos segun posicion

my_list.append(4)         ##Agregar un elemento al final de la lista
print(my_list)            ##imprimir toda la lista

my_list[0] = 'a'          ##Modificar la lista
print(my_list)

my_list.pop()             ##Eliminar el ultimo valor de la lista
print(my_list)

for element in my_list:
    print(element)

list_a = [1,2,3]
b = list_a

print(id(list_a))        ##Ver que una lista y otra es peligroso pues ahora 2 variables apuntan al
print(id(b))             ##mismo espacio de memoria

c = [1,2,3]
d = c
e = list(c)               ##CLonar una lista de esta forma evita ver dos variables apuntando al mismo objeto
f = c[::]                 ##Otra forma de clonar la lista c sin apuntar al mismo objeto de memoria


g = list(range(0, 100, 1))

doble = [i * 2 for i in g]            ##multiplica por dos todos los elementos i de la lista g
print (doble)

pares = [i for i in g if i % 2 == 0] ##Solo saca los pares de la lista g con la funcion % modulo
print(pares)
