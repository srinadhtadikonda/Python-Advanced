


from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x150+600+200")
lb1=Label(text="A")
lb1.grid(row=0,column=0,sticky=W)
e1=Entry()
e1.grid(row=0,column=1)
e1.focus()

lb2=Label(text="B")
lb2.grid(row=1,column=0,sticky=W)
e2=Entry()
e2.grid(row=1,column=1)


lb3=Label(text="C")
lb3.grid(row=2,column=0,sticky=W)
e3=Entry()
e3.grid(row=2,column=1)


lb4=Label(text="Result")
lb4.grid(row=3,column=0,sticky=W)

lb5=Label(text="")
lb5.grid(row=3,column=1,sticky=W)

def chkb():
 a=int(e1.get())
 b=int(e2.get())
 c=int(e3.get())
 if(a>b and a>c):
    messagebox.showinfo("Result","A is greater")
    lb4.config(text="A is big")
 elif(b>a and b>c):
    messagebox.showinfo("Result","B is greater")
    lb4.config(text="B is big")
 else:
    messagebox.showinfo("Result","C is greater")
    lb4.config(text="C is big")

 
def mycf():
 e1.delete(0,'end')
 e2.delete(0,'end')
 e3.delete(0,'end')
 lb5.config(text="")
 e1.focus()

def myqf():
 root.destroy()
 
btn1=Button(text="CHECK",width=10,command=chkb)
btn1.grid(row=5,column=0)

btn2=Button(text="<-",width=10,command=mycf)
btn2.grid(row=5,column=1)

btn3=Button(text="X",width=10,command=myqf)
btn3.grid(row=5,column=2)

mainloop()




