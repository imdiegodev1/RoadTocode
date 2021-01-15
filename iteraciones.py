#Loop sencillo
contador = 0
while contador < 10:
    print(contador)
    contador += 1

#loop compuesto

contador_externo = 0
contador_interno = 0

while contador_externo < 5:
    while contador_interno < 6:
        print (contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >= 3:
            break

    contador_externo += 1
    contador_interno = 0

estudiantes = {
    'mexico': 10,
    'Colombia': 15,
    'Panama': 4
}                    ##Define el diccionario

for pais in estudiantes:
    print(pais)      ##Imprime solo los paises que en este caso son las llaves del diccionario

for pais in estudiantes.keys():
    print(pais)      ##llama directamente las llaves, en el aterior tambien pero esta mas explicito

for n_estudiantes in estudiantes.values():
    print(n_estudiantes)   ##llama al valor de las llaves

for pais, n_estudiantes in estudiantes.items():
    print(pais, n_estudiantes) ##llama las llaves y al valor de forma consecutiva