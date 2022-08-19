print ('hello word')


##Data types
x = 1
y = 1.2
z = False
nothing = None

print (type(x))
print (type(y))
print (type(z))
print (type(nothing))


##Operators
print (5 + 6)
print (5 - 6)
print (2.0 * 4)
print (6 // 2)
print (6 // 4)
print (7 % 4)
print (4 ** 3)


##arithmetic operators
base = 5
high = 4
area = (base * high)/2
print ('Triangle area is', area)

##Strings
chain = '123'
print (chain + ' ' + chain)
print (f'{"Hip "*3}hurra')

my_str = 'Platzi'
print (len(my_str))
print (my_str[0])
print (my_str[2:])
print (my_str[:3])
print (my_str[:-2])
print (my_str[::2])

##Console interaction
name = input('Cual es tu nombre: ')
print ('Hola ' + name)
print ('Tu nombre tiene ', len(name), 'letras')

age = int(input('Cual es tu edad: '))
print (age)
print (type(age))