import colorama
from colorama import Fore

colorama.init(autoreset=True)

menu = {
    "Tea": 1.00, "Americano": 1.70, "Latte": 1.90, "Cappuccino": 1.90,
    "Mocha": 2.00, "Hot chocolate": 2.20, "Croissant": 1.50, "Muffin": 2.10,
    "Toast": 1.00, "Panini": 2.90, "Buttered Roll": 0.70, "Stroopwafel": 0.50
}

extras = {
    "Skimmed milk": 0.15, "2% milk": 0.20, "Full fat milk": 0.30,
    "Almond milk": 0.35, "Oat milk": 0.35, "Soya milk": 0.35,
    "Lactose-free milk": 0.40, "Custard": 1.00, "Ham 1 slice": 0.50,
    "Shredded chicken": 1.50, "Butter": 0.30, "Cheese": 1.00,
    "Salami 1 slice": 0.50, "Salad": 0.70
}

class Food:
    def __init__(self, name, temperature, allergens, calories):
        self.name = name
        self.temp = temperature
        self.allergens = allergens
        self.cal = calories

    def food_info(self):
        print(f"Item: {self.name}, Temperature: {self.temp}, "
              f"Allergens: {self.allergens}, Calories: {self.cal}")

class Drinks:
    def __init__(self, name, size, temperature, calories):
        self.name = name
        self.size = size
        self.temp = temperature
        self.calories = calories

    def drink_info(self):
        print(f"Item: {self.name}, Size: {self.size}, Temperature: {self.temp}, "
              f"Calories: {self.calories}")

def display_menu_info():
    print("\nMenu:")
    print("1. View Food Information")
    print("2. View Drink Information")
    print("3. Exit")

def get_food_info():
    print("\nFood Information:")
    for item in food_items:
        item.food_info()

def get_drink_info():
    print("\nDrink Information:")
    for item in drink_items:
        item.drink_info()

def place_order():
    total_cost = 0
    while True:
        order_input = input("What would you like to order?: ").capitalize()
        if order_input not in menu:
            print(Fore.RED + "Sorry, that item is not available.")
            continue
        order_count = int(input("How many would you like: "))
        total_cost += menu[order_input] * order_count
        print(Fore.GREEN + f"{order_count} {order_input}(s) have been added to your order. "
                            f"Current total: £{total_cost:.2f}")

        extra_order = input("Would you like to add any extras? (y/n): ")
        if extra_order.lower() == 'y':
            print("Available extras:")
            for extra in extras:
                print(f"- {extra}: £{extras[extra]:.2f}")
            while True:
                chosen_extra = input("Enter the name of the extra you'd like to add, or 'finished' to finish: ").capitalize()
                if chosen_extra == 'Finished':
                    break
                elif chosen_extra in extras:
                    total_cost += extras[chosen_extra]
                    print(Fore.GREEN + f"{chosen_extra} has been added to your order. Current total: £{total_cost:.2f}")
                else:
                    print(Fore.RED + "Sorry, that extra is not available.")
        elif extra_order.lower() != 'n' and extra_order.lower() != 'y':
            print(Fore.RED + "Invalid input. Please enter 'y' or 'n'.")

        next_order = input("Would you like to place another order? (y/n) or 'restart' to cancel all items and start again: ")
        if next_order.lower() == 'n':
            break
        elif next_order.lower() == 'restart':
            total_cost = 0
            break
    print(Fore.BLUE + f"The total is £{total_cost:.2f}. Thank you for visiting Brian's Bistro, have a good day")

if __name__ == "__main__":
    Tea = Drinks("Tea", "small", "hot", 2)
    Americano = Drinks("Americano", "medium", "hot", 18)
    Latte = Drinks("Latte", "medium", "hot", 150)
    Cappuccino = Drinks("Cappuccino", "large", "hot", 150)
    Mocha = Drinks("Mocha", "large", "hot", 233)
    Hot_Chocolate = Drinks("Hot chocolate", "large", "hot", 77)
    Bottled_Water = Drinks("Bottled Water", "medium", "cold", 0)

    Croissant = Food("Croissant", "Cold", "Dairy", 272)
    Muffin = Food("Muffin", "Cold", "Dairy", 377)
    Toast = Food("Toast", "Warm", "Dairy", 313)
    Panini = Food("Panini", "Hot", "Depends", 550)
    Buttered_Roll = Food("Buttered Roll", "Cold", "Dairy", 375)
    Stroopwafel = Food("Stroopwafel", "Cold", "Dairy", 150)
    Potato_Cake = Food("Potato Cake", "Hot", "Dairy", 123)

    food_items = [Croissant, Muffin, Toast, Panini, Buttered_Roll, Stroopwafel, Potato_Cake]
    drink_items = [Tea, Americano, Latte, Cappuccino, Mocha, Hot_Chocolate, Bottled_Water]

    while True:
        display_menu_info()
        choice = input("Please enter your choice: ")

        if choice == "1":
            get_food_info()
        elif choice == "2":
            get_drink_info()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    place_order()
