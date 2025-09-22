from Animal import Animal


class Zoo:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise TypeError("Seuls les objets Animal peuvent être ajoutés")

    def show_zoo(self):
        print(f"\n== {self} ==")
        if not self.animals:
            print("Aucun animal dans ce zoo.")
        else:
            for i, animal in enumerate(self.animals, 1):
                print(f"{i}. {animal}")

    def __add__(self, other):
        if not isinstance(other, Zoo):
            return NotImplemented

        new_name = f"{self.name} & {other.name}"
        new_city = f"{self.city}-{other.city}"
        new_zoo = Zoo(new_name, new_city)

        for animal in self.animals:
            new_zoo.add_animal(animal)
        for animal in other.animals:
            new_zoo.add_animal(animal)

        return new_zoo

    def __str__(self):
        return f"{self.name}"