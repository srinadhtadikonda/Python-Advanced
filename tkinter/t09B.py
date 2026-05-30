from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Checkbox Selection")

def update_label():
    selected = []

    for var, text in zip(vars, texts):
        if var.get() == 1:
            selected.append(text)

    label2.config(text=", ".join(selected))

vars = []
texts = ["DCA", "PGDCA", "PYTHON"]

# Create checkboxes
for text in texts:
    var = IntVar()
    vars.append(var)

    checkbox = Checkbutton(root, text=text, variable=var)
    checkbox.pack(anchor='w')

# Labels
label1 = Label(root, text="Selected Courses:")
label1.pack()

label2 = Label(root, text="")
label2.pack()

# Button
button = Button(root, text="SHOW", command=update_label)
button.pack()

root.mainloop()
