#Ejercicio de clases:
#Como se genera
class persona:
    def __init__ (self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre} me llamo {self.nombre}'

#Como se usa:

diego = persona('Diego', 35)
angelica = persona('Angelica', 26)

print(diego.saluda(angelica))


##Como se genera
class coordenada:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, otra_coordenada):
        x_diff =(self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

#como se usa

if __name__ == '__main__':
    coord_1 = coordenada(10, 15)
    coord_2 = coordenada(20,34)

    print(round(coord_1.distancia(coord_2),3))
    print(isinstance(coord_2, coordenada))