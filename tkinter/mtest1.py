import tkinter as tk
root = tk.Tk()
root.minsize(400,200)

def login():
    tw = tk.Toplevel(root)
    tw.minsize(300,100)
    entry1 = tk.Entry(tw,width=20)
    entry1.pack()

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label='New', command=login)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label='Cut')

menubar.add_cascade(label='File', menu=file_menu)
menubar.add_cascade(label='Edit', menu=edit_menu)
root.config(menu=menubar)
root.mainloop()