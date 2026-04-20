class Cleaner:
    def clean(self):
        print("Уборщик наводит порядок в зале.")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.cleaner = Cleaner()

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}, Кухня: {self.cuisine_type}, Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Новый рейтинг ресторана: {self.rating}")

    def start_cleaning(self):
        print(f"В ресторане {self.restaurant_name} начинается уборка.")
        self.cleaner.clean()

my_restaurant = Restaurant("Звезда", "Авторская", 4.5)

my_restaurant.describe_restaurant()

my_restaurant.update_rating(5.0)

my_restaurant.start_cleaning()
