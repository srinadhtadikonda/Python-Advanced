from tkinter import *

root = Tk()
root.title("Radiobutton Example")

radio_var = StringVar()
radio_var.set("Option 1")

def update_label():
    selected_value = radio_var.get()
    label.config(text=f"Selected: {selected_value}")


radio1 = Radiobutton(root, text="CASH", variable=radio_var, value="CASH", command=update_label)
radio1.pack(anchor=W)

radio2 = Radiobutton(text="CHEQUE", variable=radio_var, value="CHEQUE", command=update_label)
radio2.pack(anchor=W)

radio3 =Radiobutton(text="DD", variable=radio_var, value="DD", command=update_label)
radio3.pack(anchor=W)

label = Label(text=" ")
label.pack()

root.mainloop()
