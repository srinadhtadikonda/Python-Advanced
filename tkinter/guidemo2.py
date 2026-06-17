import tkinter as tk
root = tk.Tk()
root.title('Label Widget')
root.minsize(300,200)

lbl = tk.Label(root, text='This is Label', fg='blue', bg='yellow',
               font=('times new roman',16))

lbl.pack()
root.mainloop()
