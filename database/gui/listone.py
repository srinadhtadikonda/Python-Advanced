import mysql.connector
import tkinter as tk

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sriinformatics",
    database="demobase"
)
cursor = conn.cursor()

# Main window
root = tk.Tk()
root.geometry("400x200")

# Input Label
tk.Label(root, text='Enter Employee Number:', width=25).grid(row=1, column=1)

# Input Text Box
entry = tk.Text(root, height=1, width=4, bg='yellow')
entry.grid(row=1, column=2)

# Output Label
output = tk.StringVar(value="Output")
tk.Label(root, textvariable=output, width=30, fg='red').grid(row=3, column=1, columnspan=2)

def show_details():
    eno = entry.get('1.0', 'end').strip()
    try:
        val = int(eno)
        cursor.execute("SELECT * FROM myemp WHERE eno = %s", (val,))
        emp = cursor.fetchone()
        output.set(f"Employee Details: {emp}" if emp else "Employee not found")
    except ValueError:
        output.set("Invalid input. Please enter a valid integer.")
    except mysql.connector.Error as e:
        output.set(f"Database error: {e}")

# Show Details Button
tk.Button(root, text='Show Details', width=15, bg='red', command=show_details).grid(row=1, column=4)

# Start Tkinter main loop
root.mainloop()
