from tkinter import *
root=Tk()

lb1=Label(text="SNO")
lb1.grid(row=0,column=0)
e1=Entry()
e1.grid(row=0,column=1)

lb2=Label(text="SNAME")
lb2.grid(row=1,column=0)
e2=Entry()
e2.grid(row=1,column=1)

lb3=Label(text="SCLASS")
lb3.grid(row=2,column=0)
e3=Entry()
e3.grid(row=2,column=1)

lb4=Label(text="SSEC")
lb4.grid(row=3,column=0)
e4=Entry()
e4.grid(row=3,column=1)

lb5=Label(text="M1")
lb5.grid(row=4,column=0)
e5=Entry()
e5.grid(row=4,column=1)

lb6=Label(text="M2")
lb6.grid(row=5,column=0)
e6=Entry()
e6.grid(row=5,column=1)

lb7=Label(text="M3")
lb7.grid(row=6,column=0)
e7=Entry()
e7.grid(row=6,column=1)

lb8=Label(text="M4")
lb8.grid(row=7,column=0)
e8=Entry()
e8.grid(row=7,column=1)
 
lb9=Label(text="M5")
lb9.grid(row=8,column=0)
e9=Entry()
e9.grid(row=8,column=1)

lb10=Label(text="M6")
lb10.grid(row=9,column=0)
e10=Entry()
e10.grid(row=9,column=1)



lb11=Label(text="Total")
lb11.grid(row=10,column=0)
e11=Entry()
e11.grid(row=10,column=1)



lb12=Label(text="Average")
lb12.grid(row=11,column=0)
e12=Entry()
e12.grid(row=11,column=1)



lb13=Label(text="Grade")
lb13.grid(row=12,column=0)
e13=Entry()
e13.grid(row=12,column=1)



lb14=Label(text="Pass/Fail")
lb14.grid(row=13,column=0)
e14=Entry()
e14.grid(row=13,column=1)


def gm():
 e11.delete(0,'end')
 e12.delete(0,'end')
 e13.delete(0,'end')
 e14.delete(0,'end')
 m1=int(e5.get())
 m2=int(e6.get())
 m3=int(e7.get())
 m4=int(e8.get())
 m5=int(e9.get())
 m6=int(e10.get())
 tot=m1+m2+m3+m4+m5+m6
 e11.insert(0,tot)
 avg=tot/6
 e12.insert(0,avg)
 if(m1<35 or m2<35 or m3<35 or m4<35 or m5<35 or m6<35):
  e13.insert(0,'NIL')
  e14.insert(0,'FAIL')
 elif(avg>60):
  e13.insert(0,'A')
  e14.insert(0,'PASS')
 elif(avg<60 and avg>=45):
  e13.insert(0,'B')
  e14.insert(0,'PASS')
 elif(avg<45):
  e13.insert(0,'C')
  e14.insert(0,'PASS')

def cf():
  e1.delete(0,'end')
  e2.delete(0,'end')
  e3.delete(0,'end')
  e4.delete(0,'end')
  e5.delete(0,'end')
  e6.delete(0,'end')
  e7.delete(0,'end')
  e8.delete(0,'end')
  e9.delete(0,'end')
  e10.delete(0,'end')
  e11.delete(0,'end')
  e12.delete(0,'end')
  e13.delete(0,'end')
  e14.delete(0,'end')

btn1=Button(text="RESULT",command=gm)
btn1.grid(row=14,column=0)

btn2=Button(text="CLEAR",command=cf)
btn2.grid(row=14,column=1)

btn3=Button(text="QUIT",command=quit)
btn3.grid(row=14,column=2)

mainloop()
