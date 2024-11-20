import math
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x150+600+200")
lb1=Label(text="Principal")
lb1.grid(row=0,column=0,sticky=W)
e1=Entry()
e1.grid(row=0,column=1)
e1.focus()

lb2=Label(text="Time")
lb2.grid(row=1,column=0,sticky=W)
e2=Entry()
e2.grid(row=1,column=1)


lb3=Label(text="Rate of Interest")
lb3.grid(row=2,column=0,sticky=W)
e3=Entry()
e3.grid(row=2,column=1)


lb4=Label(text="Interest Payable")
lb4.grid(row=3,column=0,sticky=W)

lb5=Label(text="")
lb5.grid(row=3,column=1,sticky=W)

def sic():
 p=float(e1.get())
 t=float(e2.get())
 r=float(e3.get())
 si=(p*t*r)/100
 lb5.config(text=si)

def cic():
 
 p=int(e1.get())
 t=int(e2.get())
 r=int(e3.get())
 ci=p*math.pow(1+r/100,t)
 lb5.config(text=ci)
 
def mycf():
 e1.delete(0,'end')
 e2.delete(0,'end')
 e3.delete(0,'end')
 lb5.config(text="")
 e1.focus()

def myqf():
 root.destroy()
 
btn1=Button(text="Simple",width=10,command=sic)
btn1.grid(row=5,column=0)

btn2=Button(text="Compound",width=10,command=cic)
btn2.grid(row=5,column=1)

btn3=Button(text="<-",width=10,command=mycf)
btn3.grid(row=6,column=0)

btn4=Button(text="X",width=10,command=myqf)
btn4.grid(row=6,column=1)

mainloop()
