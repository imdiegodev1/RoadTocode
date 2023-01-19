
##Itera through lists
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

for element in my_list:                         ##Whit for loop
    print(element)

##Extract elements
print(next(my_iter))                            ##Whit next statement

##Easy loop
contador = 0
while contador < 10:                            ##Whit while bucle
    print(contador)
    contador += 1

##compound loop
counter_external = 0
counter_internal = 0

while counter_external < 5:
    while counter_internal < 6:
        print (counter_external, counter_internal)
        counter_internal += 1

        if counter_internal >= 3:
            break

    counter_external += 1
    counter_internal = 0


##Itera through dictionaries
estudiantes = {
    'mexico': 10,
    'Colombia': 15,
    'Panama': 4
}                                               ##Define dictionary

for pais in estudiantes:
    print(pais)                                 ##Prints only the countries which in this case are the dictionary keys.

for pais in estudiantes.keys():
    print(pais)                                 ##calls directly the keys, in the previous one also, but it is more explicit.

for n_estudiantes in estudiantes.values():
    print(n_estudiantes)                        ##calls the value of the keys

for pais, n_estudiantes in estudiantes.items():
    print(pais, n_estudiantes)                  ##calls the keys and the value consecutively