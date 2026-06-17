import pymysql

eno = int(input('Enter Employee id : '))
ena = input('Enter Employee Name : ')
sal = float(input('Enter Employee Salary : '))

sqlstr = '''insert into emp(empid, ename, salary) values (%s,%s,%s)'''

try:
    con = pymysql.connect(host='localhost', user='root',password='root123',database='demo')
    cur = con.cursor()
    cur.execute( sqlstr, (eno, ena, sal))
    con.commit()
    print('One record is added')
    cur.close()
    con.close()
except pymysql.Error:
    print('Database is not connected')