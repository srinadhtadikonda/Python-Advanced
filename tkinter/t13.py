import tkinter as tk
from tkinter import ttk

# Function to update the label text with the selected combobox value
def update_label(event):
    selected_value = combobox.get()
    label.config(text=f"Selected: {selected_value}")

# Create the main window
root = tk.Tk()
root.title("Combobox Example")

# Create a Tkinter variable to store the selected combobox value
selected_value = tk.StringVar()

# Create a combobox and populate it with options
combobox = ttk.Combobox(root, textvariable=selected_value)
combobox['values'] = ("Option 1", "Option 2", "Option 3")
combobox.current(0)  # Set the default selected value
combobox.pack()

# Bind the combobox selection event to the update_label function
combobox.bind("<<ComboboxSelected>>", update_label)

# Create a label to display the selected value
label = tk.Label(root, text="Selected: Option 1")
label.pack()

# Run the application
root.mainloop()
