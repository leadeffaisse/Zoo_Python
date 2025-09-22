from Animal import Animal


class Serpent(Animal):
    def __init__(self, weight, height):
        super().__init__(weight, height)

    def se_deplacer(self):
        print("je rampe")