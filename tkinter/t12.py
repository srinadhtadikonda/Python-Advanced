from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Combobox Example")

combobox = ttk.Combobox()
combobox['values'] = ("PEN", "PENCIL", "BOOK")
combobox.current(0)  # Set the default selected value
combobox.pack()

mainloop()
