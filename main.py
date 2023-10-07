class Human:
    def __init__(self, name="human"):
        self.name=name

    def get_name(self):
        return self.name



class Car:


    def __init__(self,model,color,year,):
        self.model = model
        self.color = color
        self.year = year
        self.passengers = []
    def show_info(self):
       print("model:",self.model)
       print("color:" , self.color)
       print("year:" , self.year)

    def set_color(self, newColor):
        self.color = newColor

    def set_model(self, model):
            self.model = model

    def set_year(self, year):
        self.year = year

    def add_passenger(self,*args):
        for human in args:
            self.passengers.append(human)

    def show_passenger(self):
        if self.passengers != []:
            print("Car -", self.model)
            for passenger in self.passengers:
                print(passenger.get_name())
        else:
            print("No passengers")


nick = Human("Nick")
kate = Human("Kate")
masha = Human("Masha")
car = Car("audi", "red", 2000)

car.add_passenger(nick, kate, masha)
car.show_passenger()


def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return(a/b)
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
 res = divider(key, data[key])
 result.append(res)\



 class Animall:
     def __init__(self, name, vid, age):
         self.name = name
         self.vid = vid
         self.age = age

     def feed(self):
         print("feed")


 class Zoo:
     def __init__(self, show_info, ):
         self.show_info = show_info

     def show_info(self):
         print(f"Name: {self.name}, vid: {self.vid}, age: {self.age}")
