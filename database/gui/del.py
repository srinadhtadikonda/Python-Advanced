import tkinter as tk
from tkinter import messagebox
import mysql.connector

def delete_record_from_mysql(eno):
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='sriinformatics',
            database='demobase'
        )
        cursor = conn.cursor()
        cursor.execute("DELETE FROM myemp WHERE eno = %s", (eno,))
        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()
        return affected_rows
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", str(err))
        return -1

def delete_record():
    eno = entry_eno.get()
    if not eno:
        messagebox.showwarning("Input Error", "Please enter an Employee Number.")
        return

    affected_rows = delete_record_from_mysql(eno)
    if affected_rows > 0:
        messagebox.showinfo("Success", f"Record with Employee Number {eno} has been deleted.")
    elif affected_rows == 0:
        messagebox.showinfo("No Record", f"No record found for Employee Number {eno}.")
    else:
        messagebox.showerror("Error", f"An error occurred while trying to delete the record.")

# Create the main application window
root = tk.Tk()
root.title("Delete Employee Record")

# Add entry and button to input eno
entry_label = tk.Label(root, text="Enter Employee Number to Delete:")
entry_label.pack(pady=5)

entry_eno = tk.Entry(root)
entry_eno.pack(pady=5)

delete_button = tk.Button(root, text="Delete Record", command=delete_record)
delete_button.pack(pady=10)

# Run the application
root.mainloop()
