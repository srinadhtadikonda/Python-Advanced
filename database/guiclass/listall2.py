import mysql.connector
import tkinter as tk
from tkinter import Entry, END

# Initialize Tkinter window
my_w = tk.Tk()
my_w.geometry("500x300")  # Adjusted width and height for better visibility

# Connect to MySQL database
my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sriinformatics",
    database="demobase"
)

my_conn = my_connect.cursor()

# Query to select data
my_conn.execute("SELECT * FROM myemp LIMIT 10")

# Fetch column names
column_names = [desc[0] for desc in my_conn.description]

# Create heading labels
for col, heading in enumerate(column_names):
    label = tk.Label(my_w, text=heading, font=('Helvetica', 10, 'bold'))
    label.grid(row=0, column=col)

# Insert data into grid
i = 1  # Start from row 1 as row 0 is for headings
for student in my_conn:
    for j in range(len(student)):
        e = Entry(my_w, width=15, fg='blue')  # Increased width for better visibility
        e.grid(row=i, column=j)
        # Convert student[j] to string before inserting
        e.insert(END, str(student[j]))
    i += 1

# Start Tkinter main loop
my_w.mainloop()
