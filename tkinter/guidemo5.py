#Demo of Checkbutton
import tkinter as tk
root = tk.Tk()
root.title('Checkbutton')
root.minsize(300,200)
def show():
    #print(cbvar.get())
    if cbvar.get():
        btn.config(state='normal')
    else:
        btn.config(state='disable')
    
cbvar = tk.BooleanVar()
cbtn = tk.Checkbutton(root, text='I Agree', onvalue=True, offvalue=False, variable=cbvar, command=show)
btn = tk.Button(root, text='Click Me', state='disable')

cbtn.pack()
btn.pack()
root.mainloop()
