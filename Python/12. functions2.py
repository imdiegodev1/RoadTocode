def enumeration (target):
    
    answ=0

    while answ**2 < target:
        print(answ)
        answ += 1
    
    if answ**2 == target:
        print(f'The square root of {target} is {answ}')
    else:
        print(f'{target} no tiene una raiz cuadrada exacta')

def aproximation (target):
    epsilon = 0.01
    step = epsilon**2
    answ = 0.0

    while abs(answ**2 - target) >= epsilon and answ <= target:
        print(abs(answ**2 - target))
        answ += step

    if abs(answ**2 - target) >= epsilon:
        print(f'The square root was not found. {target}')
    else:
        print(f'The square root of {target} is {answ}')

opcion = int(input('Choose a way to find the root: \n 1. enumeration. \n 2. approximation \n'))

if opcion == 1:
    print ('1. enumeration')
    numero = int(input('choose a number: '))
    enumeration(numero)
elif opcion == 2:
    print ('2. aproximation')
    numero = int(input('choose a number: '))
    aproximation(numero)

else:
    print('Not a valid option')

numero = int(input('Define a number: '))

def factorial(n):
    """Calculates the factorial of n.
    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1
    
    return n*factorial(n-1)

print(factorial(numero))