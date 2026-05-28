import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Course Selection")
root.geometry("350x300")

# Title Label
title_label = tk.Label(root, text="Select Courses", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Variables for checkboxes
dca_var = tk.IntVar()
java_var = tk.IntVar()
python_var = tk.IntVar()

# Function to display selected courses
def show_courses():
    selected = []

    if dca_var.get():
        selected.append("DCA")

    if java_var.get():
        selected.append("Java")

    if python_var.get():
        selected.append("Python")

    if selected:
        result_label.config(text="Selected Courses: " + ", ".join(selected))
    else:
        result_label.config(text="No Course Selected")

# Checkboxes
dca_cb = tk.Checkbutton(root, text="DCA", variable=dca_var, command=show_courses)
dca_cb.pack(anchor="w", padx=30)

java_cb = tk.Checkbutton(root, text="Java", variable=java_var, command=show_courses)
java_cb.pack(anchor="w", padx=30)

python_cb = tk.Checkbutton(root, text="Python", variable=python_var, command=show_courses)
python_cb.pack(anchor="w", padx=30)

# Result Label
result_label = tk.Label(root, text="No Course Selected", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Run application
root.mainloop()
