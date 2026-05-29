from tkinter import *

root = Tk()

d = IntVar()
p = IntVar()
j = IntVar()

cb1 = Checkbutton(root, text="DCA", variable=d)
cb1.grid(row=0, column=0, sticky=W)

cb2 = Checkbutton(root, text="PYTHON", variable=p)
cb2.grid(row=1, column=0, sticky=W)

cb3 = Checkbutton(root, text="JAVA", variable=j)
cb3.grid(row=2, column=0, sticky=W)

lb1 = Label(root, text="You Selected")
lb1.grid(row=3, column=0, sticky=W)

lb2 = Label(root, text="")
lb2.grid(row=3, column=1, sticky=W)

def csel():
    courses = []

    if d.get() == 1:
        courses.append("DCA")

    if p.get() == 1:
        courses.append("PYTHON")

    if j.get() == 1:
        courses.append("JAVA")

    lb2.config(text=", ".join(courses))

btn1 = Button(root, text="COURSE", command=csel)
btn1.grid(row=4, column=0)

root.mainloop()
