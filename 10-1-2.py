class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}, Кухня: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

newRestaurant = Restaurant("Вкусная еда", "Европейская")

print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
print("\n")

restaurant1 = Restaurant("Суши Мастер", "Японская")
restaurant2 = Restaurant("Мамма Мия", "Итальянская")
restaurant3 = Restaurant("Гриль Хаус", "Американская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
