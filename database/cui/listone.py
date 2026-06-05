import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="company"
)

cur = con.cursor()

eno = int(input("Enter Employee Number: "))

sql = "SELECT * FROM employee WHERE eno=%s"

cur.execute(sql, (eno,))

row = cur.fetchone()

if row:
    print("Employee Number :", row[0])
    print("Employee Name   :", row[1])
    print("Employee Salary :", row[2])
else:
    print("Record Not Found")

cur.close()
con.close()
