#Hello Teacher

class Animal:
    def __init__(self,name, classes, type):
        self.name = name
        self.classes = classes
        self.type = type


    def field(self):
        print(0)

    def show_info(self):
        print(f"Name: {self.name}, class: {self.classes}, type: {self.type}")


class Tiger(Animal):
    def __init__(self,name,classes, type):
        super().__init__(name, classes, type)


    def field(self):
        print("field number: 1")


class Crocodile(Animal):
    def __init__(self,name,classes, type):
        super().__init__(name, classes, type)


    def field(self):
        print("field number: 2")

class Kangaroo(Animal):
    def __init__(self,name,classes, type):
        super().__init__(name, classes, type)


    def field(self):
        print("field number: 3")


tiger1 = Tiger("gaby", "predator", "Tiger")
tiger1.show_info()
tiger1.field()

crocodile1 = Crocodile("bobby", "predator", "Crocodile")
crocodile1.show_info()
crocodile1.field()

kangaroo1 = Kangaroo("gaby", "predator", "Kangaroo")
kangaroo1.show_info()
kangaroo1.field()






