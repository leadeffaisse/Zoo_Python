from Animal import Animal
from Bird import Bird
from Snake import Snake
from Zoo import Zoo

chien = Animal("Biscuit",20, 50)

oiseau = Bird("Phoenix", 1, 30, 50)
serpent = Snake("Kaa", 1, 100)

oiseau.to_move()
serpent.to_move()

elephant = Animal("Dumbo", 1000, 300)
tigre = Animal("Tigrou", 300, 200)

Zoo1= Zoo("Paugres Safari Park", "Paugres")
Zoo1.add_animal(elephant)
Zoo1.add_animal(tigre)
Zoo1.add_animal(serpent)

Zoo2 = Zoo("Zoo d'Amnéville", "Amnéville")
Zoo2.add_animal(chien)
Zoo2.add_animal(oiseau)

Zoo3 = Zoo1 + Zoo2
Zoo3.show_zoo()
