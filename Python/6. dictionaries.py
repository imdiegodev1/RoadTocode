my_dict = {                     ##Define a Dictionary
    'David': 35,
    'Erika': 32,
    'Jaime' : 50,
}

print (my_dict['David'])        ##get the value of a key

my_dict['Jaime'] = 20           ##Redefine a value using a key
print (my_dict['Jaime'])

my_dict['Pedro'] = 50           ##Add a new element to the dict
print (my_dict)

del my_dict['Jaime']            ##Delete an element from the dict
print (my_dict)

for key in my_dict.keys():    ##Iterate through keys
    print(key)

for value in my_dict.values():  ##Iterate throuch values
    print(value)

for llave, valor in my_dict.items():                    ##Iterate using keys and values
    print((llave, valor))

print('David' in my_dict)               ##Verify if an element/key is in the dictionary
print('Diego' in my_dict)               ##Aqui se devuelven valores booleanos

country_populations = {
    'Argentina' : 7653498,
    'Brasil' : 8764542,
    'Colombia' : 8765437
}

for pais in country_populations.keys():           ##Imprimo los paises
    print(pais)

for pais in country_populations.values():         #Imprimo los valores de las llaves
    print(pais)

for pais, poblacion in country_populations.items():
    print(pais, poblacion)

string_dict= {('start', 'requiring'): 1,        ##Define a more complex dictionary
              ('requiring', 'sellers'): 8,
              ('sellers', 'post'): 14,
              ('post', 'honestly'): 1,
              ('honestly', '('): 15,
              ('(', 'especially'): 8,
                ('especially', 'those'): 2,
                ('those', 'china'): 1}

new_string = {key: value for key, value in string_dict.items() if value <= 1}       #Operate a dictionary
print(new_string)