#demo of Listbox
import tkinter as tk
root = tk.Tk()
root.title('Listbox')
root.minsize(300,200)

def show():
    indexs = lbox.curselection()
    #print(indexs)
    for ind in indexs:
        print( lbox.get(ind))
    
fruits = ['Apple','Orange','Banana','Mango']

lbox = tk.Listbox(root, width=20, height=10, selectmode=tk.MULTIPLE)
for fruit in fruits:
    lbox.insert(tk.END, fruit)

btn = tk.Button(root, text='Show', command=show)
lbox.pack()
btn.pack()
root.mainloop()
