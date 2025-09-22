from Animal import Animal


class Oiseau(Animal):
    def __init__(self, weight, height, max_altitude):
        super().__init__(weight, height)
        self.max_altitude = max_altitude

    def se_deplacer(self):
        print("je vole")