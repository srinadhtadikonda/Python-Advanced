from tkinter import *

root = Tk()

d = IntVar()
p = IntVar()
j = IntVar()

def csel():
    courses = []

    if d.get():
        courses.append("DCA")

    if p.get():
        courses.append("PYTHON")

    if j.get():
        courses.append("JAVA")

    lb2.config(text=", ".join(courses))

cb1 = Checkbutton(root, text="DCA", variable=d, command=csel)
cb1.grid(row=0, column=0, sticky=W)

cb2 = Checkbutton(root, text="PYTHON", variable=p, command=csel)
cb2.grid(row=1, column=0, sticky=W)

cb3 = Checkbutton(root, text="JAVA", variable=j, command=csel)
cb3.grid(row=2, column=0, sticky=W)

lb1 = Label(root, text="You Selected")
lb1.grid(row=3, column=0, sticky=W)

lb2 = Label(root, text="")
lb2.grid(row=3, column=1, sticky=W)

root.mainloop()
