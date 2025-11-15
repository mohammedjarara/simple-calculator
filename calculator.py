import tkinter as tk
from tkinter import messagebox

def calculate():
    operator = operator_entry.get()
    num1 = num1_entry.get()
    num2 = num2_entry.get()

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
            return
        result = num1 / num2
    else:
        messagebox.showerror("Error", f"Invalid operator: {operator}")
        return

    result_label.config(text=f"Result: {round(result,2)}")


def show_info():
    messagebox.showinfo(
        "About",
        "Simple Calculator\n\nCreated by: Mohammed Jararaa\nYear: 2025\n❤️"
    )



root = tk.Tk()
root.title("Simple Calculator - Made by Hmood")
root.geometry("350x320")


title = tk.Label(root, text="Simple Calculator", font=("Arial", 16))
title.pack(pady=10)


operator_entry = tk.Entry(root, width=10, font=("Arial", 14))
operator_entry.pack()
operator_entry.insert(0, "+")


num1_entry = tk.Entry(root, width=15, font=("Arial", 14))
num1_entry.pack(pady=5)
num1_entry.insert(0, "0")

num2_entry = tk.Entry(root, width=15, font=("Arial", 14))
num2_entry.pack(pady=5)
num2_entry.insert(0, "0")


btn = tk.Button(root, text="Calculate", font=("Arial", 14), command=calculate)
btn.pack(pady=10)


result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack()


btn_info = tk.Button(root, text="About", font=("Arial", 12), command=show_info)
btn_info.pack(pady=10)


sig = tk.Label(root, text="Made by Mohammed Jararaa © 2025", font=("Arial", 10), fg="gray")
sig.pack()

root.mainloop()
