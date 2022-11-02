##It allows you to group data and manage their behavior
##Controls the acces and prevent unwanted modifications

class PollingPlace:

    def __init__(self, id, country):
        self.__id = id
        self.__country = country
        self.__region = None

    ##Ths decorator allows you to return a hiden variable
    @property
    def region(self):
        return self.__region
    
    ##Here we check if the region is in the array 
    @region.setter
    def region(self, region):
        if region in self.__country:
            self.__region = region
        else:
            raise ValueError(f'region {region} is not valid in {self.__country}')

def main():
    place = PollingPlace(1234, ['Mexico City', 'Morelos'])
    print(place.region)

    place.region = 'Mexico City'
    print(place.region)

if __name__ == '__main__':
    main()