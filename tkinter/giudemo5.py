#adding two numbers
import tkinter as tk
root = tk.Tk()
root.title('My Calculator')
root.minsize(300,200)

def getsum():
    a = int(txta.get())
    b = int(txtb.get())
    c = a + b
    txtc.set( c)
    
lbl1 = tk.Label(root, text='First Number : ')
lbl2 = tk.Label(root, text='Second Number : ')
lbl3 = tk.Label(root, text='Result : ')

txta = tk.StringVar()
entrya = tk.Entry(root, textvariable=txta)

txtb = tk.StringVar()
entryb = tk.Entry(root, textvariable=txtb)

txtc = tk.StringVar()
entryc = tk.Entry(root, textvariable=txtc, state='disable')

btn = tk.Button(root, text='Add', command=getsum)

lbl1.pack()
entrya.pack()
lbl2.pack()
entryb.pack()
lbl3.pack()
entryc.pack()
btn.pack()


root.mainloop()
