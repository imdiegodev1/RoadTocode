x = {"jpg":10,"txt":14,"csv":2,"py":23}             ##Remember
print(x)

##Remember
print(x["txt"])
print("jpg" in x)
print("html" in x)

x["cfg"] = 8                                        ##Add a new element
print(x)

x["csv"] = 17                                       ##update the value of an element
print(x)

del x["cfg"]                                        ##Delete an element
print(x)

print(x.keys())                                     ##Remember how to get keys
print(x.values())                                   ##Remember how to get values

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}

for animal, cualidad in cool_beasts.items():        ##Iterate and use strings to present a results
    print("{} have {}".format(animal, cualidad))

##Excersice
##Count amount of letters in a string
##return the value in a dictionary
def contar_letras(texto):
    resultado = {}
    for letras in texto:
        if letras not in resultado:
            resultado[letras] = 0
        resultado[letras] += 1
    return resultado

print(contar_letras("iterating with dictionaries"))


host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())

def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed 
  # only once, and the value from guests1 taking precedence
  guests2.update(guests1)
  return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

