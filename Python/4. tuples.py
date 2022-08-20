my_tuple = (1, 'dos', True)         #Declare a tuple

print(type(my_tuple))
print(my_tuple[2])

my_tuple2 = (1,)                    ##Declare a tuple with just one element

x, y, z = my_tuple                  ##Assign a variable name to each element of the tuple

print(x)                            ##Call each element

##Starting with functions
def coordinates():
    return (5, 4)

coordenada = coordinates()

print (coordenada)

a, b = coordinates()
print (a)