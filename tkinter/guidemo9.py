import tkinter as tk
root = tk.Tk()
root.title('Listbox')
root.geometry('400x300+50+50')

def moveltr(event):
    item = list1.get( list1.curselection())
    #print(item)
    list2.insert(tk.END,item)
    list1.delete( list1.curselection())

def movertl(event):
    item = list2.get( list2.curselection())
    list1.insert(tk.END, item)
    list2.delete( list2.curselection())
    
courses = ['C','C++','Java']
list1 = tk.Listbox(root, width=20, height=10)
list2 = tk.Listbox(root, width=20, height=10)
btnltr = tk.Button(root, text='Left to Right')
btnrtl = tk.Button(root, text='Right to Left')

for i in courses:
    list1.insert(tk.END, i)
    
list1.place(x=10,y=30)
list2.place(x=250,y=30)
btnltr.place(x=160,y=50)
btnrtl.place(x=160,y=90)

btnltr.bind('<Button-1>',moveltr)
btnrtl.bind('<Button-1>',movertl)
root.mainloop()
