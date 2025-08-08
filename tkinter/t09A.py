from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Checkbox Selection")


def update_label():
    selected = []
    for var, text in zip(vars, texts):
        if var.get() == 1:
            selected.append(text)
    label.config(text=", ".join(selected))
    

vars = []
texts = ["DCA", "PGDCA", "PYTHON"]

# Create and place the checkboxes
for text in texts:
    var = IntVar()
    vars.append(var)
    checkbox = Checkbutton(text=text, variable=var, command=update_label)
    checkbox.pack(anchor='w')

# Create and place the label
label = Label(text="")
label.pack()

# Run the main loop
root.mainloop()
