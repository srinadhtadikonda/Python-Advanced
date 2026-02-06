import tkinter as tk
from tkinter import messagebox
import mysql.connector

DB_CONFIG = {"host": "localhost","user": "root","password": "12345","database": "demobase"}

def db_connect():
    return mysql.connector.connect(**DB_CONFIG)

def fetch_record_from_mysql(eno):
    try:
        with db_connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT eno, ename, esal, egrade FROM myemp WHERE eno=%s", (eno,)
            )
            return cur.fetchone()
    except mysql.connector.Error as e:
        messagebox.showerror("DB Error", str(e))

def update_record_in_mysql(old_eno, new_eno, ename, esal, egrade):
    try:
        with db_connect() as conn:
            cur = conn.cursor()
            cur.execute(
                """UPDATE myemp 
                   SET eno=%s, ename=%s, esal=%s, egrade=%s 
                   WHERE eno=%s""",
                (new_eno, ename, esal, egrade, old_eno)
            )
            conn.commit()
            return cur.rowcount
    except mysql.connector.Error as e:
        messagebox.showerror("DB Error", str(e))
        return -1

def fetch_record():
    eno = entry_eno.get()
    if not eno:
        messagebox.showwarning("Input Error", "Enter Employee Number")
        return

    row = fetch_record_from_mysql(eno)
    if not row:
        messagebox.showinfo("Not Found", "No record found")
        return

    for entry, value in zip(
        (entry_eno_new, entry_ename, entry_esal, entry_egrade), row
    ):
        entry.delete(0, tk.END)
        entry.insert(0, value)

def save_update():
    values = [e.get() for e in
              (entry_eno, entry_eno_new, entry_ename, entry_esal, entry_egrade)]

    if "" in values:
        messagebox.showwarning("Input Error", "All fields required")
        return

    rows = update_record_in_mysql(*values)
    if rows > 0:
        messagebox.showinfo("Success", "Record updated successfully")
    else:
        messagebox.showinfo("Info", "No record updated")

# UI
root = tk.Tk()
root.title("Update Employee")

labels = [
    "Employee No (Fetch)", "New Employee No",
    "Employee Name", "Salary", "Grade"
]

entries = []
for text in labels:
    tk.Label(root, text=text).pack()
    e = tk.Entry(root)
    e.pack()
    entries.append(e)

entry_eno, entry_eno_new, entry_ename, entry_esal, entry_egrade = entries

tk.Button(root, text="Fetch", command=fetch_record).pack(pady=5)
tk.Button(root, text="Update", command=save_update).pack(pady=5)

root.mainloop()
