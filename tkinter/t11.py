from tkinter import *

root = Tk()

pay = StringVar()
pay.set("CASH")

def updatepay():
    lb2.config(text=pay.get())

rb1 = Radiobutton(root, text="CASH", variable=pay, value="CASH", command=updatepay)
rb1.grid(row=0, column=0, sticky=W)

rb2 = Radiobutton(root, text="CHEQUE", variable=pay, value="CHEQUE", command=updatepay)
rb2.grid(row=1, column=0, sticky=W)

rb3 = Radiobutton(root, text="DD", variable=pay, value="DD", command=updatepay)
rb3.grid(row=2, column=0, sticky=W)

lb1 = Label(root, text="PAYMENT MODE")
lb1.grid(row=3, column=0)

lb2 = Label(root, text="")
lb2.grid(row=3, column=1)


root.mainloop()
