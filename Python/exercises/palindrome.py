def palindromo (palabra):
    palabra = palabra.replace(' ','').lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palindro = palindromo(palabra)
    if es_palindro == True:
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()