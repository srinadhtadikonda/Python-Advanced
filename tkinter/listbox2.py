#Program to change background color of window
import tkinter as tk
root = tk.Tk()
root.title('List Widget')
root.geometry(f'600x200+100+100')

def click(event):
    ind = lbcolors.curselection()
    root.config(bg=lbcolors.get(ind))
    
                
colors = ['red','green','blue','orange','black','pink','gray']

lbcolors = tk.Listbox(root,)

for color in colors:
    lbcolors.insert(tk.END, color)

lbcolors.place(x=10, y=10)

lbcolors.bind('<Button-1>',click)
root.mainloop()
