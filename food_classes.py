class Food:
    def __init__(self, temperature, allergens, calories):
        self.temp = temperature
        self.alergies = allergens
        self.cal = calories
        def food (self):
            print (f"Your item is {self.temp}, it contains {self.cal} calories and as the following allergens: {self.alergies}")
        

class Drinks: 
    def __init__(self, size, temperature, calories):
        self.size = size
        self.temp = temperature
        self.calories = calories
    def hot (self):
        print (f"Here is your {self.size} 'drink', careful it is {self.temp}. Calories: {self.calories} ")

Tea = Drinks("small", "hot", 2)
Americano = Drinks("medium", "hot", 18)
Latte = Drinks("medium", "hot", 150)
Cappuccino = Drinks("large", "hot", 150)
Mocha = Drinks("large", "hot", 233)
Hot_Chocolate = Drinks("large", "hot", 77)
Bottled_Water = Drinks("medium", "cold", 0)

Croissant = Food ("Cold", "Dairy", 272)
Muffin = Food ("Cold", "Dairy", 377)
Toast = Food ("Warm", "Dairy", 313)
Panini = Food ("Hot", "Depends", 550)
Buttered_Roll = Food ("Cold", "Dairy", 375)
Stroopwafel = Food ("Cold", "Dairy", 150)
Poatao_Cake = Food ("Hot", "Dairy", 123)