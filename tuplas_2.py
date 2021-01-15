##son grupos de datos inmutables

tupla = ("Esto", "es", "una", "tupla")
print(tupla)

##Iterar con listas y tuplas

animals = ["Lion", "Zebra", "Delfin", "mico"]
chars = 0

for animal in animals:
    chars += len(animal)

print("Caracteres totales: {}, longitud promedio: {}".format(chars, chars/len(animals)))

winners = ["Diego", "Dylan", "Angelica"]
for index, person in enumerate(winners):
    print("{} - {}". format(index+1,person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("diegoanr40@hotmail.com", "Diego naranjo"),("angeCas@toutlock.com","Angelica C")]))