import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="company"
)

cur = con.cursor()

eno = int(input("Enter Employee Number to Delete: "))

sql = "DELETE FROM employee WHERE eno=%s"

cur.execute(sql, (eno,))

con.commit()

if cur.rowcount > 0:
    print("Record Deleted Successfully")
else:
    print("Record Not Found")

cur.close()
con.close()
