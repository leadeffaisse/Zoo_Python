from Animal import Animal


class Snake(Animal):
    def __init__(self, name, weight, height):
        super().__init__(name, weight, height)

    def to_move(self):
        print("je rampe")