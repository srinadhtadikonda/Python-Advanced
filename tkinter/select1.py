# demo of reading data from a table
import pymysql

sqlstr = 'select * from emp'
try:
    #creating a bridge between python and database
    con = pymysql.connect(host='localhost', user='root', password='root123', database='demo')
    
    #create cursor object to execute queries
    cur = con.cursor()

    #executing a query
    cur.execute(sqlstr)

    #fetching records from cursor
    rs = cur.fetchall()

    for r in rs:
        print(f'Employee id : {r[0]}')
        print(f'Employee Name : {r[1]}')
        print(f'Employee Salary : {r[2]}')

    cur.close()
    con.close()
except pymysql.Error as e:
    print(f'Error : {e}')