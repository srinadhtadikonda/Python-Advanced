import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            entry_var.set("")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify="right")
entry.pack(fill="both", ipadx=8, ipady=8, pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(button_frame)
    frame.pack(side="top", fill="both", expand=True)
    for btn in row:
        button = tk.Button(frame, text=btn, font=("Arial", 18), padx=10, pady=10)
        button.pack(side="left", fill="both", expand=True)
        button.bind("<Button-1>", on_click)

root.mainloop()
