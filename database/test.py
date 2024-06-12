import mysql.connector
x=mysql.connector.connect(host="localhost",user="root",passwd="sriinformatics",database="demobase")
print(x)
