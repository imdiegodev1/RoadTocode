numero = int(input('Define un numero: '))

def factorial(n):
    """Calcula el factorial de n.
    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1
    
    return n*factorial(n-1)

print(factorial(numero))