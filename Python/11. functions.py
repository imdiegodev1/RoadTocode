def multiply_by_two (n):                        ##Declare a function that multiply by 2 any number
    return n*2

def add_two (n):                                ##Declare a function that add 2 to any number
    return n+2

def apply_operation (f,numeros):                ##This function receives 2 parameters: which function to use and the array of numbers.
    resultado = []                              ##here we define that the function will use an array
    for numero in numeros:                      ##we define a cycle to go through the array
        resultado = f(numero)                   ##we define the result to be a function already declared.
        resultado.append(resultado)             ##


sumar = lambda x, y: x + y                      ##This is how to use anonymous functions

def apply_operations(num):
    
    operaciones = [abs, float]                  ##We use the abs function inside an array that will use an array function.

    resultado = []                              ##we define that the function is going to use an array
    for operacion in operaciones:               ##we define the bucle
        resultado.append(operacion(num))        ##We define what the bucle will do, it calls the same function in which it is encapsulated.
    
    return resultado