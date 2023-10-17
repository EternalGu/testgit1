class Human:
    def __init__(self, full_name, birthday, contact_number, city, country, address):
        self.full_name = full_name
        self.birthday = birthday
        self.contact_number = contact_number
        self.city = city
        self.country = country
        self.address = address

    def show_info(self):
        print("ПІБ:", self.full_name)
        print("Дата народження:", self.birthday)
        print("Контактний телефон:", self.contact_number)
        print("Місто:", self.city)
        print("Країна:", self.country)
        print("Домашня адреса:", self.address)

class City:
    def __init__(self, name, region, country, population, pochtovii_index, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.pochtovii_index= pochtovii_index
        self.phone_code = phone_code

    def show_info(self):
        print("Назва міста:", self.name)
        print("Назва регіону:", self.region)
        print("Назва країни:", self.country)
        print("Кількість жителів:", self.population)
        print("Поштовий індекс:", self.pochtovii_index)
        print("Телефонний код:", self.phone_code)


person = Human("Іван Петрович", "01.01.2000", "+380123456789", "Дніпро", "Україна", "Вулиця колопопопопоп")
print("People information:")
person.show_info()


city = City("Дніпро", "Дніпропетровська область", "Україна", 1000000, "03000", "+38098")
print("City information:")
city.show_info()



