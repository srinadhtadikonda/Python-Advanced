#Creating a menubar
import tkinter as tk

root = tk.Tk()
root.title('Menu Demo')
root.minsize(600,200)

def close():
    root.destroy()

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
edit_menu = tk.Menu(menubar, tearoff=0)

file_menu.add_command(label='New',)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=close)
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')

menubar.add_cascade(label='File', menu=file_menu)
menubar.add_cascade(label='Edit', menu=edit_menu)
root.config(menu=menubar)
root.mainloop()