usuario_1 = input('Cual es tu nombre usuario 1: ')
edadu_1 = int(input('Cual es tu edad: '))
usuario_2 = input('Cual es tu nombre usuario 2: ')
edadu_2 = int(input('Cual es tu edad: '))

if edadu_1 > edadu_2:
    print('El usuario ' + usuario_1 + ' es mayor que ' + usuario_2)
elif edadu_1 < edadu_2:
    print('El usuario ' + usuario_2 + 'es mayor que ' + usuario_1)
else:
    print ('Ambos usuarios tienen la misma edad')

