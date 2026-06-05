import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="company"
)

cur = con.cursor()

eno = int(input("Enter Employee Number to Update: "))
newname = input("Enter New Name: ")
newsal = float(input("Enter New Salary: "))

sql = "UPDATE employee SET ename=%s, esal=%s WHERE eno=%s"

cur.execute(sql, (newname, newsal, eno))

con.commit()

if cur.rowcount > 0:
    print("Record Updated Successfully")
else:
    print("Record Not Found")

cur.close()
con.close()
