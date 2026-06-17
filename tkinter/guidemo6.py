import tkinter as tk
root = tk.Tk()
root.title('Radiobutton')
root.minsize(300,200)
def show():
    print(rbgender.get())
    
rbgender = tk.StringVar()
rbMale = tk.Radiobutton(root, text='Male', variable=rbgender, value='Male', command=show)
rbFemale = tk.Radiobutton(root, text='Female',variable=rbgender, value='Female', command=show)

rbMale.pack()
rbFemale.pack()
root.mainloop()
