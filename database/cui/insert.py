import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="company"
)

cur = con.cursor()

eno = int(input("Enter Employee Number: "))
ename = input("Enter Employee Name: ")
esal = float(input("Enter Employee Salary: "))

sql = "INSERT INTO employee VALUES(%s,%s,%s)"
values = (eno, ename, esal)

cur.execute(sql, values)

con.commit()

print("Record Inserted Successfully")

cur.close()
con.close()
