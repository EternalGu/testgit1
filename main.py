class Car:
    color = "white"



    def __init__(self,model,color,year):
        self.model = model
        self.color = color
        self.year = year
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

myCar = Car("audi","red",2022)
myCar.color = "red"

myCar.show_info()

myCar2 = Car("lamborghini","yellow", 2021)
myCar2.color = "yellow"

myCar2.show_info()
