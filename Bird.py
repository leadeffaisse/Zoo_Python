from Animal import Animal


class Bird(Animal):
    def __init__(self, name, weight, height, max_altitude):
        super().__init__(name, weight, height)
        self.__max_altitude = max_altitude

    def to_move(self):
        print("je vole")

    @property
    def max_altitude(self):
        return self.__max_altitude

    @max_altitude.setter
    def max_altitude(self, max_altitude):
        self.__max_altitude = max_altitude