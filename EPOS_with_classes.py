import colorama
from colorama import init, Fore

colorama.init(autoreset=True)

# Define the Menu class
class Menu:
    def __init__(self, name, temperature, allergens, calories):
        self.temp = temperature
        self.allergies = allergens
        self.cal = calories
        self.name = name

    def menu(self):
        print(f"{self.name} is {self.temp}, it contains {self.cal} calories and has the following extra information: {self.allergies}")

# Define menu items
menu = {
    "Tea": 1.00,
    "Americano": 1.70,
    "Latte": 1.90,
    "Cappuccino": 1.90,
    "Mocha": 2.00,
    "Hot chocolate": 2.20,
    "Croissant": 1.50,
    "Muffin": 2.10,
    "Toast": 1.00,
    "Panini": 2.90,
    "Buttered Roll": 0.70,
    "Stroopwafel": 0.50
}

extras = {
    "Skimmed milk": 0.15,
    "2% milk": 0.20,
    "Full fat milk": 0.30,
    "Almond milk": 0.35,
    "Oat milk": 0.35,
    "Soya milk": 0.35,
    "Lactose-free milk": 0.40,
    "Custard": 1.00,
    "Ham 1 slice": 0.50,
    "Shredded chicken": 1.50,
    "Butter": 0.30,
    "Cheese": 1.00,
    "Salami 1 slice": 0.50,
    "Salad": 0.70
}

def start():
    while True:
        welcome_message = input("""Hello and welcome to 'Brian's Bistro', unfortunately our card machine is broken today and we are only accepting cash. Here is the menu:
    _______________________________________________________
    │  Drinks                  │  Food                    │
    │ - Tea           : £1.00  │ - Croissant     : £1.50  │
    │ - Americano     : £1.70  │ - Muffin        : £2.10  │
    │ - Latte         : £1.90  │ - Toast         : £1.00  │
    │ - Cappuccino    : £1.90  │ - Panini        : £2.90  │
    │ - Mocha         : £2.00  │ - Buttered Roll : £0.70  │
    │ - Hot Chocolate : £2.20  │ - Stroopwafel   : £0.50  │
    │ - Bottled Water : £1.00  │ - Potato Cake   : £1.00  │

    Would you like to place an order y/n: """)
        if welcome_message == "y":
            print("Good choice")
        elif welcome_message == "n":
            continue
        else:
            print("Invalid input, enter 'y' or 'n' ")
            continue
        break

    # Display menu information
    menu_info = input("Would you like to see information about our menu first? (y/n): ")
    if menu_info.lower() == "y":
        for item in menu_items:
            item.menu()

    total_cost = 0
    while True:
        order_input = input("What would you like to order?: ").capitalize()
        if order_input.capitalize() not in menu:
            print(Fore.RED + "Sorry, that item is not available.")
            continue
        order_count = int(input("How many would you like: "))
        total_cost += menu[order_input] * order_count
        print(Fore.GREEN + f"{order_count} {order_input}(s) have been added to your order. Current total: £{total_cost:.2f}")

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
        elif extra_order.lower() != 'n':
            print(Fore.RED + "Invalid input. Please enter 'y' or 'n'.")

        next_order = input("Would you like to place another order? (y/n) or 'restart' to cancel all items and start again: ")
        if next_order.lower() == 'n':
            break
        elif next_order.lower() == 'restart':
            total_cost = 0
            start()
    print(Fore.BLUE + f"The total is £{total_cost:.2f}. Thank you for visiting Brian's Bistro, have a good day")

if __name__ == "__main__":
    # Define instances of Menu
    Tea = Menu("Tea", "small", "hot", 2)
    Americano = Menu("Americano","medium", "hot", 18)
    Latte = Menu("Latte", "medium", "hot", 150)
    Cappuccino = Menu("Cappuccino", "large", "hot", 150)
    Mocha = Menu("Mocha", "large", "hot", 233)
    Hot_Chocolate = Menu("Hot Chocolate", "large", "hot", 77)
    Bottled_Water = Menu("Bottled Water", "medium", "cold", 0)
    Croissant = Menu("Croissant", "Cold", "Dairy", 272)
    Muffin = Menu("Muffin", "Cold", "Dairy", 377)
    Toast = Menu("Toast", "Warm", "Dairy", 313)
    Panini = Menu("Panini", "Hot", "Depends on ingredients", 550)
    Buttered_Roll = Menu("Buttered Roll", "Cold", "Dairy", 375)
    Stroopwafel = Menu("Stroopwafel", "Cold", "Dairy", 150)
    Potato_Cake = Menu("Potato Cake", "Hot", "Dairy", 123)

    # Create a list of menu items to iterate over
    menu_items = [Tea, Americano, Latte, Cappuccino, Mocha, Hot_Chocolate, Bottled_Water, Croissant, Muffin, Toast, Panini, Buttered_Roll, Stroopwafel, Potato_Cake]

    # Start the ordering process
    start()
