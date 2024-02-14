class Food:
    def __init__(self, name, temperature, category, calories):
        self.name = name
        self.temperature = temperature
        self.category = category
        self.calories = calories

    def food_info(self):
        print(f"Name: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Category: {self.category}")
        print(f"Calories: {self.calories}")

class Drinks:
    def __init__(self, name, size, temperature, calories):
        self.name = name
        self.size = size
        self.temperature = temperature
        self.calories = calories

    def drink_info(self):
        print(f"Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Temperature: {self.temperature}")
        print(f"Calories: {self.calories}")
