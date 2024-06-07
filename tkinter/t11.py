import tkinter as tk

# Function to update the label text with the selected radiobutton value
def update_label():
    selected_value = radio_var.get()
    label.config(text=f"Selected: {selected_value}")

# Create the main window
root = tk.Tk()
root.title("Radiobutton Example")

# Create a Tkinter variable to store the selected radiobutton value
radio_var = tk.StringVar()

# Set the default value of the radiobuttons
radio_var.set("Option 1")

# Create radiobuttons
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1", command=update_label)
radio1.pack(anchor=tk.W)

radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2", command=update_label)
radio2.pack(anchor=tk.W)

radio3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3", command=update_label)
radio3.pack(anchor=tk.W)

# Create a label to display the selected value
label = tk.Label(root, text="Selected: Option 1")
label.pack()
