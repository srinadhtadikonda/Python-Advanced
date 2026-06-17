import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Treeview')
root.minsize(150, 300)
treeview = ttk.Treeview(root)

languages = treeview.insert('','end',text='Languages')
c = treeview.insert(languages,'end',text='C')
cpp = treeview.insert(languages,'end',text='C++')
java = treeview.insert(languages, 'end', text='Java')

web = treeview.insert('','end',text='Web Designing')
html = treeview.insert(web,'end', text='HTML')

treeview.pack()
root.mainloop()
