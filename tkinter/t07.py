from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("300x150+600+200")

lb1=Label(text="A")
lb1.grid(row=0,column=0,sticky=W)
e1=Entry()
e1.grid(row=0,column=1)


lb2=Label(text="B")
lb2.grid(row=1,column=0,sticky=W)
e2=Entry()
e2.grid(row=1,column=1)


lb3=Label(text="C")
lb3.grid(row=2,column=0,sticky=W)
e3=Entry()
e3.grid(row=2,column=1)

def mysum():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a+b
 e3.insert(0,c)

def mysub():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a-b
 e3.insert(0,c)

def mymul():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a*b
 e3.insert(0,c)

def mydiv():
 try:
  e3.delete(0,'end')
  a=int(e1.get())
  b=int(e2.get())
  c=a/b
  e3.insert(0,c)
 except:
  messagebox.showinfo("Error","You Cannot divide a number with zero")
  e2.delete(0,'end')
  e2.focus()

def myfdiv():
 try:
  e3.delete(0,'end')
  a=int(e1.get())
  b=int(e2.get())
  c=a//b
  e3.insert(0,c)
 except:
  messagebox.showinfo("Error","You Cannot divide a number with zero")
  e2.delete(0,'end')
  e2.focus()

def mymod():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a%b
 e3.insert(0,c)

def myexp():
 e3.delete(0,'end')
 a=int(e1.get())
 b=int(e2.get())
 c=a**b
 e3.insert(0,c)

def mycf():
 e1.delete(0,'end')
 e2.delete(0,'end')
 e3.delete(0,'end')
 tbx1.focus()

def myqf():
 root.destroy()
 
btn1=Button(text="+",width=10,command=mysum)
btn1.grid(row=3,column=0)

btn2=Button(text="-",width=10,command=mysub)
btn2.grid(row=3,column=1)

btn3=Button(text="*",width=10,command=mymul)
btn3.grid(row=3,column=2)

btn4=Button(text="/",width=10,command=mydiv)
btn4.grid(row=4,column=0)

btn5=Button(text="//",width=10,command=myfdiv)
btn5.grid(row=4,column=1)

btn6=Button(text="%",width=10,command=mymod)
btn6.grid(row=4,column=2)

btn7=Button(text="**",width=10,command=myexp)
btn7.grid(row=5,column=0)

btn8=Button(text="<-",width=10,command=mycf)
btn8.grid(row=5,column=1)

btn9=Button(text="X",width=10,command=myqf)
btn9.grid(row=5,column=2)

mainloop()
