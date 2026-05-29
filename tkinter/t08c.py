from tkinter import *

root = Tk()

courses = {"DCA": IntVar(), "PYTHON": IntVar(), "JAVA": IntVar()}

for i, (name, var) in enumerate(courses.items()):
    Checkbutton(root, text=name, variable=var).grid(row=i, column=0, sticky=W)

Label(root, text="You Selected").grid(row=3, column=0, sticky=W)
result = Label(root, text="")
result.grid(row=3, column=1, sticky=W)

def csel():
    result.config(
        text=", ".join(name for name, var in courses.items() if var.get())
    )

Button(root, text="COURSE", command=csel).grid(row=4, column=0)

root.mainloop()
