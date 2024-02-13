import tkinter as tk
from tkinter import messagebox

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


class BriansBistroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Brian's Bistro")

        self.order_label = tk.Label(master, text="Order:")
        self.order_label.pack()

        self.order_text = tk.Text(master, height=10, width=40)
        self.order_text.pack()

        self.total_cost_label = tk.Label(master, text="Total Cost:")
        self.total_cost_label.pack()

        self.total_cost_value = tk.Label(master, text="£0.00")
        self.total_cost_value.pack()

        self.menu_frame = tk.LabelFrame(master, text="Menu")
        self.menu_frame.pack(pady=10)

        for item in menu:
            button = tk.Button(self.menu_frame, text=f"{item} - £{menu[item]:.2f}", command=lambda i=item: self.prompt_extras(i))
            button.pack(anchor=tk.W)

        self.selected_item = None
        self.selected_extras = []

        self.print_receipt_button = tk.Button(master, text="Print Receipt", command=self.print_receipt)
        self.print_receipt_button.pack()

    def prompt_extras(self, item):
        self.selected_item = item
        self.extra_window = tk.Toplevel(self.master)
        self.extra_window.title(f"Extras for {item}")
        self.extra_frame = tk.Frame(self.extra_window)
        self.extra_frame.pack()

        self.extra_vars = {}

        for extra in extras:
            self.extra_vars[extra] = tk.IntVar()
            extra_checkbox = tk.Checkbutton(self.extra_frame, text=f"{extra} - £{extras[extra]:.2f}", variable=self.extra_vars[extra])
            extra_checkbox.extra_name = extra
            extra_checkbox.extra_cost = extras[extra]
            extra_checkbox.pack(anchor=tk.W)

        confirm_button = tk.Button(self.extra_window, text="Confirm", command=self.add_extras)
        confirm_button.pack()

    def add_extras(self):
        total_cost = menu[self.selected_item]
        self.order_text.insert(tk.END, f"{self.selected_item} - £{menu[self.selected_item]:.2f}\n")
        for extra in extras:
            if self.extra_vars[extra].get() == 1:
                extra_name = extra
                extra_cost = extras[extra]
                self.order_text.insert(tk.END, f"\t{extra_name} - £{extra_cost:.2f}\n")
                total_cost += extra_cost
        self.update_total_cost(total_cost)
        self.extra_window.destroy()

    def update_total_cost(self, amount):
        current_total = float(self.total_cost_value["text"][1:])
        new_total = current_total + amount
        self.total_cost_value.config(text=f"£{new_total:.2f}")

    def print_receipt(self):
        receipt = self.order_text.get("1.0", tk.END)
        total_cost = self.total_cost_value["text"]
        messagebox.showinfo("Receipt", f"{receipt}\nTotal Cost: {total_cost}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BriansBistroApp(root)
    root.mainloop()

