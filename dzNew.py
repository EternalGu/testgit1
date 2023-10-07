class Animal:
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
#__str__ посомтрел в интренете так как выдавало ошибку искал как исправить
    def __str__(self):
        return f"{self.name} {self.type} {self.age}"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} join the world")

    def show_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)


tiger = Animal("rudy", "Lion", 5)
crocodile = Animal("kamp", "corocodile", 10)
kangaroo = Animal("agata", "kangaroo", 7)

zoo = Zoo()
zoo.add_animal(tiger)
zoo.add_animal(crocodile)
zoo.add_animal(kangaroo)

zoo.show_animals()






