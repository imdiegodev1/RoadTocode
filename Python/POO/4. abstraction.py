##Abstraction allows us to focus con important aspects of the problem


##This example shows a washing machine process
class WashingMachine:

    def __init__(self):
        pass

    def wash (self, temperature='hot'):
        self._fill_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._dry()

    def _fill_water_tank(self, temperature):
        print(f'Filling water tank at {temperature}')

    def _add_soap(self):
        print('adding soap')

    def _wash(self):
        print('Washing clothes')

    def _dry(self):
        print('Dring clothes')


def main():
    washing_machine = WashingMachine()
    washing_machine.wash()

if __name__ == '__main__':
    main()