##Los diccionarios se definen con {}
x = {"jpg":10,"txt":14,"csv":2,"py":23}
print(x)
##La logica de los diccionarios es muy similar a los strings y listas.
##Aqui algunos ejemplos para ilustrar
print(x["txt"])
print("jpg" in x)
print("html" in x)
x["cfg"] = 8    ##Agregar un nuevo elemento al diccionario
print(x)
x["csv"] = 17   ##Si agrego un elemento existente va a actualizar el valor
print(x)
del x["cfg"]    ##Eliminar un elemento del diccionario
print(x)

##Iteraciones con diccionarios
##Volvemos a utilizar el diccioanrio x

for extencion in x:     ##Imprimir solo las llaves de los diccioanrios
    print(extencion)

for value in x.values():
    print(value)

for ext, amount in x.items():
    print("Aqui hay {} archivos con el .{} extencion".format(amount, ext))

##como sea, hay dos metodos para acceder o a las llaves
##o a los valores
print(x.keys())
print(x.values())

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for animal, cualidad in cool_beasts.items():
    print("{} have {}".format(animal, cualidad))

##contar el numero de letras en un string y
##mostrarlas en un diccionario
def contar_letras(texto):
    resultado = {}
    for letras in texto:
        if letras not in resultado:
            resultado[letras] = 0
        resultado[letras] += 1
    return resultado

print(contar_letras("iterando con diccionarios"))


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

def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
