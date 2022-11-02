##Classes also can have functions that defines how to interact 
##internaly and with other classes

##little example to find the distance between two points in a
##cartesian plane
class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_coordinate):
        x_diff = (self.x + other_coordinate.x)**2
        y_diff = (self.y + other_coordinate.y)**2

        return (x_diff + y_diff)**0.5

def main():
    coordinate_1 = Coordinates(50, 20)
    coordinate_2 = Coordinates(4, 25)

    print(coordinate_1.distance(coordinate_2))

    ##To know if an instance belongs to a certain class we can use
    ##isinstance(instance, class)
    print(isinstance(coordinate_2, Coordinates))

if __name__ == '__main__':
    main()