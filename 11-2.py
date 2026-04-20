class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours
        self.popsicles = []
        self.soft_ice_creams = []

    def show_info(self):
        print(f"Кафе: {self.restaurant_name}, Адрес: {self.location}, Часы работы: {self.working_hours}")

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Вкус '{flavor}' добавлен.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Вкус '{flavor}' удален.")
        else:
            print(f"Вкуса '{flavor}' нет в списке.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Вкус '{flavor}' есть в наличии!")
        else:
            print(f"Вкуса '{flavor}' сейчас нет.")

    def add_popsicle(self, name):
        self.popsicles.append(name)
        print(f"Мороженое на палочке '{name}' добавлено.")

    def add_soft_ice_cream(self, name):
        self.soft_ice_creams.append(name)
        print(f"Мягкое мороженое '{name}' добавлено.")

    def show_types(self):
        print(f"На палочке: {self.popsicles}")
        print(f"Мягкое: {self.soft_ice_creams}")


stand = IceCreamStand("Льдинка", "Десерты", ["Ваниль"], "Центральный парк", "10:00 - 20:00")

stand.show_info()
stand.add_flavor("Фисташка")
stand.check_flavor("Фисташка")
stand.remove_flavor("Ваниль")

stand.add_popsicle("Фруктовый лед")
stand.add_soft_ice_cream("Сливочный рожок")
stand.show_types()
