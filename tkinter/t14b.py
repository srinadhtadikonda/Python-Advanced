from tkinter import *

root=Tk()

lbx=Listbox(selectmode=MULTIPLE)
lbx.pack()

def uilist(event):
 si=lbx.curselection()
 sv=[lbx.get(i) for i in si]
 lb.config(text=f"Selected:{','.join(sv)}")


items=['pen','pencil','paper','eraser','sharpner']

for i in items:
    lbx.insert(END,i)

lbx.bind("<<ListboxSelect>>",uilist)

lb=Label(text="selected:")
lb.pack()
mainloop()
