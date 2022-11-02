##you can be as general as you want in terms of class creation
##or also be as specific as you want. In poo inheritance allows you to relate
##some classes to bigger or more general classes in order to
##control functionality or attributes.

##in this example we will show how the rectangle class will be
##the parent of the square class
class Rectangle:

    def __init__ (self, base, high):
        self.base = base
        self.high = high

    def area(self):
        return self.base * self.high

##inheritance in python is declare with the following format
class Square(Rectangle):

    ##constructor method in inheritance:
    def __init__(self, base):
        super().__init__(base, base)

def main():
    
    rectangle = Rectangle(base=5, high=10)
    print(rectangle.area())

    square = Square(base=10)
    print(square.area())

if __name__ == '__main__':
    main()