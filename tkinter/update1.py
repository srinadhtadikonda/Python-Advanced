import pymysql

def update_rec(eno, ena, sal):
    sqlstr = 'update emp set ename=%s, salary=%s where empid = %s'
    try:
        con = pymysql.connect(host='localhost', user='root', password='root123', database='demo')
        cur = con.cursor()
        cur.execute(sqlstr, (ena, sal, eno))
        con.commit()

        cur.close()
        con.close()
        print('One record is updated successfully')
        
    except pymysql.Error:
        print('Database is not connected')
if __name__ =='__main__':
    eno = int(input('Enter Employee id to update :'))
    ena = input('Enter New Employee Name : ')
    sal = float(input('Enter New Employee Salary :'))

    update_rec(eno, ena, sal)
