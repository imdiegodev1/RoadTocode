##programa solo para percibir como un problema se puede decomponer en 
##problemas mas pequeños

class automovil:

    def __init__ (self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'                 ##Esto es una variable privada de la clase
        self._motor = None

    def acelerar (self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en movimiento'

class motor:

    def __init__(self, cilindros, tipo = 'gasolina'):      ##Aqui hay un parametro de la clase definido por defecto como gasolina
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass