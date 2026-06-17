#demo of combobox
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Combobox')
root.minsize(500, 300)

lbl = tk.Label(root, text = 'Colors : ')
combobox = ttk.Combobox(root, values=('red','green','blue','Orange','black'))
lbl.grid(row=0, column=0)
combobox.grid(row=1, column=0, padx=10)

def showcolor(event):
    #print( combobox.get())
    root.config( bg=combobox.get())
    
combobox.bind('<Button-1>', showcolor)

root.mainloop()
