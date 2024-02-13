import tkinter as tk
from tkinter import messagebox

# Define your menu
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

class CafeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Cafe Application")

        self.total_cost = 0

        self.create_widgets()

    def create_widgets(self):
        # Create labels and buttons
        self.menu_label = tk.Label(self, text="Menu:")
        self.menu_label.grid(row=0, column=0, sticky="w")

        self.order_label = tk.Label(self, text="Order:")
        self.order_label.grid(row=0, column=1, sticky="w")

        self.order_listbox = tk.Listbox(self, height=10)
        self.order_listbox.grid(row=1, column=1, padx=10, sticky="nsew")

        self.total_label = tk.Label(self, text="Total: £0.00")
        self.total_label.grid(row=2, column=1, sticky="e")

        for item, price in menu.items():
            btn = tk.Button(self, text=f"{item} - £{price:.2f}", command=lambda item=item, price=price: self.add_to_order(item, price))
            btn.grid(sticky="w")

        self.finish_order_button = tk.Button(self, text="Finish Order", command=self.finish_order)
        self.finish_order_button.grid(row=3, column=1, sticky="e")

        self.restart_button = tk.Button(self, text="Restart", command=self.restart_order)
        self.restart_button.grid(row=4, column=1, sticky="e")

    def add_to_order(self, item, price):
        self.total_cost += price
        self.order_listbox.insert(tk.END, f"{item} - £{price:.2f}")
        self.total_label.config(text=f"Total: £{self.total_cost:.2f}")

    def finish_order(self):
        messagebox.showinfo("Total", f"Your total is £{self.total_cost:.2f}. Thank you!")
    
    def restart_order(self):
        self.order_listbox.delete(0, tk.END)
        self.total_cost = 0
        self.total_label.config(text="Total: £0.00")

if __name__ == "__main__":
    app = CafeApp()
    app.mainloop()
