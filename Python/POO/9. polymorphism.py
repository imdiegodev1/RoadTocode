##Polymorphism allows you to create different forms using the same object
##We can change the behavior of a Super class insigh a sub class

##in this example we can see how a person move and how a cyclist move
##both use move function but sub class is changing the method
class Person:

    def __init__(self, name):
        self.name = name

    def move(self):
        print('moving forward')


class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def move(self):
        print('moving forward fast')

def main():
    
    person = Person('Juan')
    person.move()

    cyclist = Cyclist('Carlos')
    cyclist.move()

if __name__ == '__main__':
    main()