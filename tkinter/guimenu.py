import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pymysql
#import mysql.connector

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.title('Employee Database Management')
        self.root.minsize(800,400)

        self.lbl1 = tk.Label(self.root, text='Employee Database Management System',
                             font=('times new roman',20), bg='black', fg='yellow')
        self.lbl1.pack(side=tk.TOP,fill=tk.X)

        
        self.left_frame = tk.Frame(self.root, width=300,height=200, bg='#123456')
        self.left_frame.place(x=10,y=50)

        self.buttons_frame = tk.Frame(self.root, width=300, height=100, bg='#123421')
        self.buttons_frame.place(x=10,y=270)
        self.btn_add = tk.Button(self.buttons_frame, text='Save Record', width=12)
        self.btn_search = tk.Button(self.buttons_frame, text='Search Record', width=12)
        self.btn_update = tk.Button(self.buttons_frame, text='Update Record', width=12)
        self.btn_delete = tk.Button(self.buttons_frame, text='Delete Record', width=12)
        self.btn_showall = tk.Button(self.buttons_frame, text=' Show All ', width=12)
        self.btn_dbcon = tk.Button(self.buttons_frame, text='DB Connect', width=12)
        self.btn_dbdiscon = tk.Button(self.buttons_frame, text='DB Disconnect', width=12)

        self.btn_add.place(x=5,y=5)
        self.btn_search.place(x=105,y=5)
        self.btn_update.place(x=205,y=5)
        self.btn_delete.place(x=5, y=35)
        self.btn_showall.place(x=105, y=35)
        self.btn_dbcon.place(x=205,y=35)
        self.btn_dbdiscon.place(x=5, y=65)

        self.right_frame = tk.Frame(self.root, width=360, height=320, bg='#123456')
        self.right_frame.place(x=320,y=50)
        self.treeview = ttk.Treeview(self.right_frame,columns=('empno','ename','salary'), show='headings')
        self.treeview.heading('empno', text='Emplooyee ID')
        self.treeview.heading('ename',text='Employee Name')
        self.treeview.heading('salary',text='Salary')
        self.treeview.column('empno',width=100)
        self.treeview.column('ename', width=200)
        self.treeview.column('salary',width=150)

        self.treeview.pack()
        
        self.lbl_emp_details = tk.Label(self.left_frame,text='Employee Details', bg='red', fg='white',
                                        font=('times new roman',16))
        
        

        self.lbl_eno = tk.Label(self.left_frame, text='Employee Number :', fg='black',width=20)
        self.lbl_ena = tk.Label(self.left_frame, text='Employee Name   :', fg='black', width=20)
        self.lbl_sal = tk.Label(self.left_frame, text='Employee Salary : ', fg='black', width=20)
        self.vareno = tk.StringVar()
        self.varena = tk.StringVar()
        self.varsal = tk.StringVar()

        self.entry_eno = tk.Entry(self.left_frame,width=20, textvariable=self.vareno)
        self.entry_ena = tk.Entry(self.left_frame, width=20, textvariable=self.varena)
        self.entry_sal = tk.Entry(self.left_frame, width=20, textvariable=self.varsal)


        self.lbl_emp_details.place(x=10, y=10)
        self.lbl_eno.place(x=10, y=50)
        self.lbl_ena.place(x=10, y=80)
        self.lbl_sal.place(x=10, y=110)
        self.entry_eno.place(x=170,y=50)
        self.entry_ena.place(x=170, y=80)
        self.entry_sal.place(x=170, y=110)

        self.btn_dbcon.bind('<Button-1>', self.dbcon)
        self.btn_add.bind('<Button-1>', self.save)
        self.btn_search.bind('<Button-1>', self.search)
        self.btn_update.bind('<Button-1>', self.update)
        self.btn_delete.bind('<Button-1>', self.delete)
        self.btn_showall.bind('<Button-1>',self.showall)
        self.btn_dbdiscon.bind('<Button-1>', self.dbdiscon)

    def dbcon(self, event):
        try:
            self.con = pymysql.connect(host='localhost', user='root', password='root123', database='demo')
            messagebox.showinfo('BCE', 'Database is connected')
        except pymysql.Error as e:
            messagebox.showerror('BCE', e)

    def dbdiscon(self, event):
        self.con.close()
        messagebox.showinfo('BCE','Database is diconnected')

    def save(self, event):
        eno = int(self.vareno.get())
        ena = self.varena.get()
        sal = float(self.varsal.get())
        sqlstr = 'insert into emp(empid, ename, salary) values (%s, %s, %s)'

        cur = self.con.cursor()
        cur.execute(sqlstr, (eno, ena, sal))
        self.con.commit()
        cur.close()
        messagebox.showinfo("BCE", 'One Record is added')

    def search(self,event):
        if self.vareno.get() != '':
            eno = int(self.vareno.get())
            sqlstr = 'select ename, salary from emp where empid = %s'
            cur = self.con.cursor()
            cur.execute(sqlstr, (eno,))
            rs = cur.fetchone()
            self.varena.set( rs[0])
            self.varsal.set( rs[1])
            cur.close()
        else:
            messagebox.showinfo('BCE','Enter employee id')

    def update(self, event):
        eno = self.vareno.get()
        ena = self.varena.get()
        sal = self.varsal.get()
        sqlstr = 'update emp set ename = %s, salary = %s where empid = %s'
        cur = self.con.cursor()
        cur.execute(sqlstr, (ena,sal, eno))
        self.con.commit()
        messagebox.showinfo('BCE', 'One Record is not updated')
        cur.close()

    def delete(self, event):
        eno = int(self.vareno.get())
        sqlstr = 'delete from emp where empid= %s'
        cur = self.con.cursor()
        cur.execute(sqlstr, (eno,))
        self.con.commit()
        messagebox.showinfo('BCE','One record is deleted')
        cur.close()

    def showall(self, event):
        sqlstr = 'select *from emp'
        cur = self.con.cursor()
        cur.execute(sqlstr)
        rs = cur.fetchall()
        for r in rs:
            self.treeview.insert('','end',values=r)

        cur.close()
if __name__ == '__main__':
    root = tk.Tk()
    emp = Employee(root)
    root.mainloop()