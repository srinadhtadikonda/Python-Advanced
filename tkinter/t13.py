import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Combobox Example")

def update_label(event):
    selected_value = combobox.get()
    label.config(text=f"Selected: {selected_value}")

selected_value = tk.StringVar()

combobox = ttk.Combobox(root, textvariable=selected_value)a
combobox['values'] = ("PEN", "PENCIL", "BOOK")
combobox.current(0)  # Set the default selected value
combobox.pack()
combobox.bind("<<ComboboxSelected>>", update_label)
label = tk.Label(root, text=" ")
label.pack()

root.mainloop()
