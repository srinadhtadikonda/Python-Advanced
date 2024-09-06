import mysql.connector
import tkinter as tk
from tkinter import * 

# Establishing MySQL connection
my_connect = mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd="sriinformatics",
    database="demobase"
)
my_cursor = my_connect.cursor()

# Create the main window
my_w = tk.Tk()
my_w.geometry("400x200") 

# Add a Label
l1 = tk.Label(my_w, text='Enter Employee Number:', width=25)  
l1.grid(row=1, column=1) 

# Add a Text Box
t1 = tk.Text(my_w, height=1, width=4, bg='yellow') 
t1.grid(row=1, column=2) 

# Define the function to show details
def my_details():
    eno = t1.get('1.0', 'end').strip()  # Get the input from the Text widget and strip newlines
    try:
        val = int(eno)  # Check input is integer or not
        try:
            query = "SELECT * FROM myemp WHERE eno = %s"
            my_cursor.execute(query, (val,))
            myemp = my_cursor.fetchone()
            if myemp:
                my_str.set(f"Employee Details: {myemp}")
            else:
                my_str.set("Employee not found")
        except mysql.connector.Error as db_err:
            my_str.set(f"Database error: {db_err}")
    except ValueError:
        my_str.set("Invalid input. Please enter a valid integer.")

# Add a Button
b1 = tk.Button(my_w, text='Show Details', width=15, bg='red', command=my_details)
b1.grid(row=1, column=4) 

# Create a StringVar for output
my_str = tk.StringVar()
my_str.set("Output")

# Add a Label for output
l2 = tk.Label(my_w, textvariable=my_str, width=30, fg='red')  
l2.grid(row=3, column=1, columnspan=2)

# Start the Tkinter main loop
my_w.mainloop()
