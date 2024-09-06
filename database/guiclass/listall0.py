import mysql.connector
import tkinter as tk
from tkinter import Entry, END

# Initialize Tkinter window
my_w = tk.Tk()
my_w.geometry("500x300")

# Connect to MySQL database
my_connect = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sriinformatics",
    database="demobase"
)

my_conn = my_connect.cursor()
my_conn.execute("SELECT * FROM myemp LIMIT 10")

# Insert data into grid
for i, row in enumerate(my_conn, start=1):  # start=1 to begin at row 1
    for j, value in enumerate(row):
        e = Entry(my_w, width=15, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, str(value))

# Start Tkinter main loop
my_w.mainloop()
