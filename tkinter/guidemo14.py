import tkinter as tk
from tkinter import ttk 

root= tk.Tk()
root.minsize(400,200)
root.title('Treeview Widget')

treeview = ttk.Treeview(root, columns=('slno','ename','salary'), show='headings')
treeview.heading('slno', text='Employee No')
treeview.heading('ename', text='Employee Name')
treeview.heading('salary', text='Salary')

treeview.insert('','end',values=(10100, 'Ravi', 45000.0))
treeview.insert('','end', values=(12100, 'Ashok Kuamr', 45300.00) )

treeview.pack() 
root.mainloop()