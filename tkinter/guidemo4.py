#demo of Entry widget

import tkinter as tk

root = tk.Tk()
root.title('Brilliant')
root.minsize(300,200)
def wish():
    na = txtvar.get()
    print(f'Hello, {na}')
    
lbl = tk.Label(root, text='Enter your Name :')
txtvar = tk.StringVar()
entry = tk.Entry(root, textvariable=txtvar)
btn = tk.Button(root, text='Say Hello', command=wish)

lbl.pack()
entry.pack()
btn.pack()
root.mainloop()
