import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

def fetch_data_from_mysql(eno):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sriinformatics',
            database='demobase'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT eno, ename, esal, egrade FROM myemp WHERE eno = %s", (eno,))
        row = cursor.fetchone()
        conn.close()
        return row
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
        return None

def display_data():
    for widget in frame.grid_slaves():
        if int(widget.grid_info()["row"]) > 1:
            widget.grid_forget()

    eno = entry_eno.get()
    if not eno:
        messagebox.showwarning("Input Error", "Please enter an Employee Number.")
        return

    row = fetch_data_from_mysql(eno)
    if row:
        for j, value in enumerate(row):
            label = tk.Label(frame, text=value, borderwidth=1, relief="solid")
            label.grid(row=2, column=j, sticky="nsew")
    else:
        messagebox.showinfo("No Record", f"No record found for Employee Number {eno}")

# Create the main application window
root = tk.Tk()
root.title("Employee Record")

# Create a frame for the grid
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Add headers
headers = ['Employee Number', 'Employee Name', 'Employee Salary', 'Employee Grade']
for i, header in enumerate(headers):
    label = tk.Label(frame, text=header, borderwidth=1, relief="solid")
    label.grid(row=1, column=i, sticky="nsew")

# Add entry and button to input eno
entry_label = tk.Label(root, text="Enter Employee Number:")
entry_label.pack(pady=5)

entry_eno = tk.Entry(root)
entry_eno.pack(pady=5)

fetch_button = tk.Button(root, text="Fetch Record", command=display_data)
fetch_button.pack(pady=10)

# Run the application
root.mainloop()
