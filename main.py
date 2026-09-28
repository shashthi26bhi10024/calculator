import tkinter as tk
from tkinter import messagebox

import advanced
import calculationhistory
import memory



window = tk.Tk()
window.title("Calculator")
window.geometry("420x680")

display = tk.Entry(window, font=("Arial", 24), justify="right")
display.pack(fill="x", padx=15, pady=15)


def add_text(x):
    display.insert(tk.END, x)


def clear():
    display.delete(0, tk.END)


def backspace():
    display.delete(len(display.get()) - 1, tk.END)


def calculate():
    try:
        expression = display.get()
        result = eval(
            expression.replace("%", "/100"),
            {"__builtins__": {}}
        )
        display.delete(0, tk.END)
        display.insert(0, result)
        calculationhistory.add_to_history(
            f"{expression} = {result}"
        )
    except:
        messagebox.showerror("Error", "Invalid calculation")


buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "(", ")", "%", "⌫"
]

frame = tk.Frame(window)
frame.pack()

for i, text in enumerate(buttons):

    if text == "=":
        command = calculate
    elif text == "⌫":
        command = backspace
    else:
        command = lambda x=text: add_text(x)

    tk.Button(
        frame,
        text=text,
        width=5,
        height=2,
        font=("Arial", 16),
        command=command
    ).grid(
        row=i // 4,
        column=i % 4,
        padx=4,
        pady=4
    )


tk.Button(
    window,
    text="Clear",
    command=clear
).pack(pady=10)


window.mainloop()