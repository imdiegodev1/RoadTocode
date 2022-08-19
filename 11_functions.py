def multiplicar_por_dos (n):         ##una funcion normal
    return n*2

def sumar_dos (n):                   ##una funcion normal
    return n+2

def aplicar_operacion (f,numeros):   ##Esta funcion recibe 2 parametros: que funcion a usar y el arreglo de numeros
    resultado = []                   ##Aqui defino que la funcion va a usar un array
    for numero in numeros:           ##defino que un ciclo para recorrer el arreglo
        resultado = f(numero)        ##defino que el resultaod va a ser una funcion ya declarada
        resultado.append(resultado)  ##


sumar = lambda x, y: x + y           ##Aqui uso la funcion lamnda como definicion de la variable sumar

def aplicar_operaciones(num):
    operaciones = [abs, float]       ##Utilizo la funcion abs dentro de un arreglo que utilizara una funcion

    resultado = []                   ##defino que la funcion va a usar un array
    for operacion in operaciones:    ##defino un ciclo
        resultado.append(operacion(num))     ##defino lo que el ciclo hara, llama la misma funcion en la cual esta encapsulado
    
    return resultado