class Tiger:
    def __init__(self, name, classes, type):
        self.name = name
        self.classes = classes
        self.type = type

    def show_info(self):
        print(f"Name: {self.name}, class: {self.classes}, type: {self.type}")


class Crocodile:
    def __init__(self, name, classes, type):
        self.name = name
        self.classes = classes
        self.type = type

    def show_info(self):
        print(f"Name: {self.name}, class: {self.classes}, type: {self.type}")


class Kangaroo:
    def __init__(self, name, classes, type):
        self.name = name
        self.classes = classes
        self.type = type

    def show_info(self):
        print(f"Name: {self.name}, class: {self.classes}, type: {self.type}")


tiger1 = Tiger("mani", "predator", "Tiger")
tiger1.show_info()


crocodile1 = Crocodile("", "predator", "Crocodile")
crocodile1.show_info()


kangaroo1 = Kangaroo("agata", "herbivorous", "Kangaroo")
kangaroo1.show_info()

class Zoo:
    def __init__(self):

