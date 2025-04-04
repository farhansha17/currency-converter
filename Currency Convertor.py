import tkinter as tk
from tkinter import messagebox
import requests


def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url).json()
        rate = response['rates'].get(to_currency)

        if rate:
            converted_amount = round(amount * rate, 2)
            result_label.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")
        else:
            messagebox.showerror("Error", "Invalid currency selection")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")


# GUI setup
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x250")

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

from_currency_var = tk.StringVar(root)
to_currency_var = tk.StringVar(root)

currencies = ["USD", "EUR", "GBP", "INR", "AUD", "CAD", "JPY"]

from_currency_var.set("USD")
to_currency_var.set("INR")

tk.Label(root, text="From Currency:").pack()
tk.OptionMenu(root, from_currency_var, *currencies).pack()

tk.Label(root, text="To Currency:").pack()
tk.OptionMenu(root, to_currency_var, *currencies).pack()

tk.Button(root, text="Convert", command=convert_currency).pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
