def run():
    x = 0
    i = 0
    while x <= 1000 and i <= 1000:   ## imprimir todos las potencias de 2 hasta 1000
        x += 1
        i = 2 ** (x)
        print (i)
    print('Programa terminado')

if __name__ == "__main__":
    run()

#print([el for el in range(10) if el % 2 ==0])

#global = 'hello'
#print (global)

print(5//2)