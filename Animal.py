class Animal:
    def __init__(self, name, weight, height):
        self._name = name
        self._weight = weight
        self._height = height

    def to_move(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if not weight > 0:
            raise ValueError("Weight must be positive")
        self._weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if not height > 0:
            raise ValueError("Height must be positive")
        self._height = height

    def __str__(self):
        return f"{str(self.name)} pèse {self.weight} kg et mesure {self.height} cm."