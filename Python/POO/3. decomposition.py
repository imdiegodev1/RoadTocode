
##Decompostion means to divide a problem in little problems
##that solve the original problem step by step

##This example is about a car that moves and use multiple
##clases to explain its functionality
class Car:

    def __init__(self, model, brand, color):
        self.model = model
        self.brand = brand
        self.color = color
        ##Here we can declare some private attributes
        self._state = "waiting"
        self._engine = Engine(cilinders=4)

        def speed_up(self, type='slow'):
            if type == 'fast':
                self._engine.inject_gas(10)
            else:
                self._engine.inject_gas(3)

            self._state = 'movementimage.png'

class Engine:

    def __init__(self, cilinders, type='gas'):
        self.cilinders = cilinders
        self.type = type
        self._temperature = 0

    def inject_gas(self, amount):
        pass