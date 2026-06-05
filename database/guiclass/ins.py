from tkinter import *
import mysql.connector
from tkinter import messagebox
p=mysql.connector.connect(host="localhost",user="root",password="brilliant",database="demobase",port=3306)
q=p.cursor()
root = Tk()
root.title("Insert")
root.geometry("750x350")

label1 = Label(root, text="ENO", width=20,height=2).grid(row=1, column=0)
label2 = Label(root, text="ENAME", width=20,height=2).grid(row=2, column=0)
label3 = Label(root, text="ESAL", width=20,height=2).grid(row=3, column=0)
label4 = Label(root, text="EGRADE", width=20, height=2).grid(row=4, column=0)

e1 = Entry(root, width=30, borderwidth=5)
e1.grid(row=1, column=2)

e2 = Entry(root, width=30, borderwidth=5)
e2.grid(row=2, column=2)

e3 = Entry(root, width=30, borderwidth=5)
e3.grid(row=3, column=2)

e4 = Entry(root, width=30, borderwidth=5)
e4.grid(row=4, column=2)

def insrec():
    r="insert into myemp(eno,ename,esal,egrade) values (%s,%s,%s,%s)"
    eno = e1.get()
    ename = e2.get()
    esal = e3.get()   
    egrade=e4.get()
    s=(eno,ename,esal,egrade)
    q.execute(r,s)
    p.commit()
    messagebox.showinfo("Success","Record Inserted")
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    
btn1=Button(text="INSERT",command=insrec)
btn1.grid(row=5,column=0)
mainloop()
