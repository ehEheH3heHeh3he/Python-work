import random
import tkinter as tk
from tkinter import Label, Entry, Button

# Function to calculate change
def calculate_change():
    try:
        cost = float(cost_entry.get())
        payment = float(payment_entry.get())

        change = payment - cost

        if change < 0:
            result_label.config(text="Insufficient payment. Please provide enough funds.")
        else:
            num_thousand_banknotes = change // 1000
            change %= 1000

            num_hundred_banknotes = change // 100
            change %= 100

            num_twenty_banknotes = change // 20
            change %= 20

            num_coins = change

            result_label.config(text=f"Change breakdown:\n"
                                      f"1000 Banknotes: {int(num_thousand_banknotes)}\n"
                                      f"100 Banknotes: {int(num_hundred_banknotes)}\n"
                                      f"20 Banknotes: {int(num_twenty_banknotes)}\n"
                                      f"1 Coin: {int(num_coins)}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
window = tk.Tk()
window.title("Change Calculator")

# Cost Entry
cost_label = Label(window, text="Cost:")
cost_label.pack()
cost_entry = Entry(window)
cost_entry.pack()

# Payment Entry
payment_label = Label(window, text="Payment:")
payment_label.pack()
payment_entry = Entry(window)
payment_entry.pack()

# Calculate Button
calculate_button = Button(window, text="Calculate Change", command=calculate_change)
calculate_button.pack()

# Result Label
result_label = Label(window, text="")
result_label.pack()

window.mainloop()
