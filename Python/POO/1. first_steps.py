##How to declare a class
class Restaurant:
    pass


##atributes of a class are created in the constructor
##method

class Restaurant:

    def __init__(self, location, restaurant_type, n_chairs):
        self.location = location
        self.restaurant_type = restaurant_type
        self.n_chairs = n_chairs


##To create an object
def main():
    chinese = Restaurant('downtown', 'Chinese', '50')

##If we want to get an attribute of the new instance
    print(chinese.restaurant_type)


if __name__ == '__main__':
    main()