import tkinter as tk

# Function to update the label text with the selected listbox values
def update_label(event):
    # Get the selected items
    selected_indices = listbox.curselection()
    selected_values = [listbox.get(i) for i in selected_indices]
    
    # Update the label text
    label.config(text=f"Selected: {', '.join(selected_values)}")

# Create the main window
root = tk.Tk()
root.title("Listbox Example")

# Create a listbox with multiple selection mode
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()

# Populate the listbox with options
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
for option in options:
    listbox.insert(tk.END, option)

# Bind the listbox selection event to the update_label function
listbox.bind("<<ListboxSelect>>", update_label)

# Create a label to display the selected values
label = tk.Label(root, text="Selected: ")
label.pack()

# Run the application
root.mainloop()
