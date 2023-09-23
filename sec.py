class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age#private

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self.__age)

    def set_name(self, newName):
        self.name = newName

    def set_age(self, newAge):
        if newAge > 0 and newAge < 100:
            self.__age = newAge
        else:
            print("Error data age")


st1 = Student("Ilon Mask", 20)
st1.name = "Batman"
st1.get_name()

st1.set_age(40)
st1.get_age()



class Player:
    def __init__(self, name, rasa):
        self.name = name
        self.rasa = rasa

    def atack(self):
        print("i am player")

    def show_info(self):
        print(f"Name: {self.name}, rasa: {self.rasa}")


class Elf(Player):
    def __init__(self, name, rasa):
        super().__init__(name, rasa)

    def atack(self):
        print("I am elf! I am attacking with bow")


class Human(Player):
    def __init__(self, name, rasa):
        super().__init__(name, rasa)

    def atack(self):
        print("I am human! I am attacking with sword")


elf1 = Elf("gobby", "elf")
elf1.show_info()
elf1.atack()

human1 = Human("Anton", "human")
human1.show_info()
human1.atack()


class Figura:
    def __init__(self, color, pi, x, y):
        self.color = color
        self.pi = 3.14
        self.x = x
        self.y = y

    def color(self):
        print("white")


    def x(self):
        print(99)

    def y(self):
        print(70)

    def show_info(self):
        print(f"Color: {self.color}, X: {self.x}, y: {self.y}")


class Triangle(Figura):
    def __init__(self, color, pi, x, y):
        super().__init__(color, pi,  x, y)

    def color(self):
        print("yellow")

    def x(self):
        print(134)

    def y(self):
        print(50)


class Circle(Figura):
    def __init__(self, color, pi,  x, y):
        super().__init__(color, pi, x, y)

    def color(self):
        print("red")

    def x(self):
        print(12)

    def y(self):
        print(40)


class Rectangle(Figura):
    def __init__(self, color, pi, x, y):
        super().__init__(color, pi, x, y)

    def color(self):
        print("blue")

    def x(self):
        print(90)

    def y(self):
        print(120)


triangle1 = Triangle("yellow", 134, 50)
triangle1.show_info()

circle1 = Circle("red", 12, 40)
circle1.show_info()
















