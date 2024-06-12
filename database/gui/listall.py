import tkinter as tk
from tkinter import ttk
import mysql.connector

def fetch_data_from_mysql():
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='sriinformatics',
        database='demobase'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT eno, ename, esal, egrade FROM myemp")
    rows = cursor.fetchall()
    conn.close()
    return rows

def display_data():
    rows = fetch_data_from_mysql()
    
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            label = tk.Label(frame, text=value, borderwidth=1, relief="solid")
            label.grid(row=i+1, column=j, sticky="nsew")

# Create the main application window
root = tk.Tk()
root.title("Employee List")

# Create a frame for the grid
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Add headers
headers = ['Employee Number', 'Employee Name', 'Employee Salary', 'Employee Grade']
for i, header in enumerate(headers):
    label = tk.Label(frame, text=header, borderwidth=1, relief="solid")
    label.grid(row=0, column=i, sticky="nsew")

# Display the data
display_data()

# Run the application
root.mainloop()
