class Menu:
    def __init__(self, name, temperature, allergens, calories):
        self.name = name
        self.temp = temperature
        self.allergies = allergens
        self.cal = calories

    def menu(self):
        print(f"{self.name} is {self.temp}, it contains {self.cal} calories and has the following extra information: {self.allergies}")

# Define instances of Menu
Tea = Menu("Tea", "small", "hot", 2)
Americano = Menu("Americano", "medium", "hot", 18)
Latte = Menu("Latte", "medium", "hot", 150)
Cappuccino = Menu("Cappuccino", "large", "hot", 150)
Mocha = Menu("Mocha", "large", "hot", 233)
Hot_Chocolate = Menu("Hot Chocolate", "large", "hot", 77)
Bottled_Water = Menu("Bottled Water", "medium", "cold", 0)
Croissant = Menu("Croissant", "Cold", "Dairy", 272)
Muffin = Menu("Muffin", "Cold", "Dairy", 377)
Toast = Menu("Toast", "Warm", "Dairy", 313)
Panini = Menu("Panini", "Hot", "Depends", 550)
Buttered_Roll = Menu("Buttered Roll", "Cold", "Dairy", 375)
Stroopwafel = Menu("Stroopwafel", "Cold", "Dairy", 150)
Potato_Cake = Menu("Potato Cake", "Hot", "Dairy", 123)

# Ask user if they want to see menu information
menu_info = input("Would you like to see information about our menu? (y/n): ")
if menu_info.lower() == "y":
    # Create a list of menu items to iterate over
    menu_items = [Tea, Americano, Latte, Cappuccino, Mocha, Hot_Chocolate, Bottled_Water, Croissant, Muffin, Toast, Panini, Buttered_Roll, Stroopwafel, Potato_Cake]
    # Iterate over menu items and display information
    for item in menu_items:
        item.menu()
