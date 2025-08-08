from tkinter import *

root = Tk()

# Variable to store the selected value
payment_method = StringVar(value="cash")  # default empty

rb1 = Radiobutton(root, text="CASH", variable=payment_method, value="cash")
rb1.pack(anchor=W)

rb2 = Radiobutton(root, text="CHEQUE", variable=payment_method, value="cheque")
rb2.pack(anchor=W)

rb3 = Radiobutton(root, text="DD", variable=payment_method, value="dd")
rb3.pack(anchor=W)

root.mainloop()
