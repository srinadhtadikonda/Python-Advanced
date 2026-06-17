import tkinter as tk
root = tk.Tk()
root.minsize(300,300)
root.title('Listbox Methods')

def addcourse():
    lbox.insert(tk.END, txtvar.get())
    txtvar.set('')

def count():
    n = lbox.size()
    #print(n)
    txtvar.set( f'There are {n} courses')

lbl1 = tk.Label(root, text='Courses :')
lbl2 = tk.Label(root, text='Course Title:')

courses = ['C','C++','Java']
lbox = tk.Listbox(root, height=10, width=20)
for course in courses:
    lbox.insert(tk.END, course)

txtvar = tk.StringVar()
entry1 = tk.Entry(root, textvariable=txtvar)
btnadd = tk.Button(root, text='Add Course', command=addcourse)
btncount = tk.Button(root, text='Count', command=count)

lbl1.place(x=10, y=10)
lbox.place(x=10, y=40)
lbl2.place(x=150, y=40)
entry1.place(x=150,y=60)
btnadd.place(x=150, y=80)
btncount.place(x=150, y=110)
root.mainloop()
