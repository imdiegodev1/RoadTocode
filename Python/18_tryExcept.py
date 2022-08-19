
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i/divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)                  ##aqui se genera la excepcion, en esta funcion cuando se divide entre 0
        return lista

lista = list(range(10))
divisor=2
divisor2 = 0        ##probar codigo con division en 0??

print(divide_elementos_de_lista(lista, divisor2))
