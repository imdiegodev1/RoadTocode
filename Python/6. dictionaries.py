my_dict = {                     ##Define a Dictionary
    'David': 35,
    'Erika': 32,
    'Jaime' : 50,
}


string_dict= {('start', 'requiring'): 1,        ##Define a more complex dictionary
              ('requiring', 'sellers'): 8,
              ('sellers', 'post'): 14,
              ('post', 'honestly'): 1,
              ('honestly', '('): 15,
              ('(', 'especially'): 8,
                ('especially', 'those'): 2,
                ('those', 'china'): 1}

new_string = {key: value for key, value in string_dict.items() if value <= 1}
print(new_string)

print (my_dict['David'])

my_dict['Jaime'] = 20         ## Reasignar valores de una llave
print (my_dict['Jaime'])

my_dict['Pedro'] = 50           ##Agregue a Pedro al diccionario
print (my_dict)

del my_dict['Jaime']            ##Elimino a alguien del diccionario
print (my_dict)

for llave in my_dict.keys():    ##Itero utilizando las llaves
    print(llave)

for valor in my_dict.values():    ##Itero utilizando los valores
    print(valor)

for llave, valor in my_dict.items():    ##Iterar tanto con llave como valor
    print((llave, valor)+('Esto es lo que importa'))

print('David' in my_dict)               ##Verificar si una llave esta en el diccionario
print('Diego' in my_dict)               ##Aqui se devuelven valores booleanos

poblacion_paises = {
    'Argentina' : 7653498,
    'Brasil' : 8764542,
    'Colombia' : 8765437
}

for pais in poblacion_paises.keys():           ##Imprimo los paises
    print(pais)

for pais in poblacion_paises.values():         #Imprimo los valores de las llaves
    print(pais)

for pais, poblacion in poblacion_paises.items():
    print(pais, poblacion)
    