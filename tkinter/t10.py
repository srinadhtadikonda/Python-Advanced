from tkinter import *
root=Tk()
rb1=Radiobutton(text="CASH",value="cash")
rb1.pack(anchor=W)
rb2=Radiobutton(text="CHEQUE",value="cheque")
rb2.pack(anchor=W)
rb3=Radiobutton(text="DD",value="dd")
rb3.pack(anchor=W)
mainloop()