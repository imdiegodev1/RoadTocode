
class Ejercicio:                            ##Clase principal com su metodo constructor

    def __init__ (self, nivel, duracion):
        self.nivel = nivel
        self.duracion = duracion

    def hace_ejercicio(self):
        print('Esta haciendo ejercicio')

class Aerobico(Ejercicio):                  ##Clase hija que hereda metodos de clase ejercicio

    def __init__(self, nivel, duracion, tipo = 'aerobico'):             ##Metodo constructor de la clase aerobico
        super().__init__(nivel, duracion)                               ##referencio/llamo el metodo constructor de la clase ejercicio
        self.tipo = tipo                                                ##Defino un parametro extra, modifico el metodo constructor

    def hace_ejercicio(self):                                           ##Polimorfismo, uso y modifico el metodo hace_ejercicio que proviene de clase ejercicio
        print(f'Esta haciendo ejercicio {self.tipo} con una duraciòn {self.duracion} y un nivel {self.nivel}')

class Anaerobico(Ejercicio):

    def __init__(self, nivel, duracion, tipo = 'Anaerobico'):
        super().__init__(nivel, duracion)

    def hace_ejercicio(self):
        print(f'Esta haciendo ejercicio anaerobico')

def main():
    ejercicio = Ejercicio('suave', 'moderada')
    ejercicio.hace_ejercicio()

    aerobico = Aerobico('moderado','larga')
    aerobico.hace_ejercicio()

    anaerobico = Anaerobico('fuerte', 'intervalos')
    anaerobico.hace_ejercicio()

if __name__ == '__main__':
    main()
