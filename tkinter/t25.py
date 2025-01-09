from tkinter import *

root = Tk()
m = Menu(root)
root.config(menu=m)

filemenu = Menu(m,tearoff=0)
m.add_cascade(label='File', m=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(m,tearoff=0)
m.add_cascade(label='Help', m=helpmenu)
helpmenu.add_command(label='About')

mainloop()
