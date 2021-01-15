class lavadora:
    def __init__(self):
        pass

    def lavar (self, temperatura = 'fria'):
        self._llenar_tanque_agua(temperatura)
        self._add_jabon()
        self._lavar()
        self._centrifugado()

    def _llenar_tanque_agua(self, temperatura):
        print(f'Llenando el tanque de agua a {temperatura}')
    
    def _add_jabon(self):
        print('Añadiendo jabon')
    
    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugado(self):
        print('secando la ropa')

if __name__ == '__main__':
    lavadora=lavadora()
    lavadora.lavar()
