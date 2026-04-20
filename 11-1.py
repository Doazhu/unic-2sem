class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}, Кухня: {self.cuisine_type}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Доступные вкусы мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")

my_ice_cream = IceCreamStand("Снежинка", "Десерты", ["Ваниль", "Шоколад", "Клубника"])
my_ice_cream.show_flavors()
