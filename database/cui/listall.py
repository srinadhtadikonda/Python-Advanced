import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="company"
)

cur = con.cursor()

cur.execute("SELECT * FROM employee")

rows = cur.fetchall()

print("ENO\tENAME\tSALARY")
print("-"*30)

for row in rows:
    print(row[0], "\t", row[1], "\t", row[2])

cur.close()
con.close()
