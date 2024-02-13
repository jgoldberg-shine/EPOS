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

def start():
    while True:
        welcome_message = input("""Hello and welcome to the cafe, here is the menu:
                                _____________________________________________________
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
            start()
        else:
            print("invalid input, enter 'y' or 'n' ")
            continue
        break

    total_cost = 0
    while True:
        order_input = input("What would you like to order?: ")
        if order_input not in menu:
            print("Sorry, that item is not available.")
            continue
        order_count = int(input("How many would you like: "))
        total_cost += menu[order_input] * order_count
        print(f"{order_count} {order_input}(s) have been added to your order. Current total: £{total_cost:.2f}")
        
        next_order = input("Would you like to place another order? (y/n) or 'restart' to cancel all items and start again: ")
        if next_order.lower() == 'n':
            break
        elif next_order.lower() == 'restart':
            total_cost = 0
            start()
    print(f"The total is £{total_cost:.2f}. Thank you for visiting our cafe, have a good day")

start()