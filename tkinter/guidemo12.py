#demo of Spinbox
import tkinter as tk

root = tk.Tk()
root.title('Spinbox')
root.minsize(300,200)

sbox = tk.Spinbox(root, from_ = 1, to=20)
tbox = tk.Text(root, height=10, width=20)
sbox.pack()
tbox.pack()
def show(event):
    n = int(sbox.get())+1
    #print(n)
    s=''
    for i in range(1, 11):
        s += f'{n} x {i} = {n*i}\n'
    tbox.insert(1.0, s)
    
sbox.bind('<Button-1>', show)
root.mainloop()
