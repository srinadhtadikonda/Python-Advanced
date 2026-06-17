import pymysql 

def add_record(eno, ena, sal):
    sqlstr = 'insert into emp(empid, ename, salary) values (%s,%s,%s)'
    global con 
    con = pymysql.connect(host='localhost',user='root', password='root123', database='demo')
    cur = con.cursor()
    cur.execute(sqlstr, (eno, ena, sal))
    con.commit()
    print('One Record is added')
    cur.close()

def show_all():
    global con
    sqlstr = 'select *from emp'
    cur = con.cursor()
    cur.execute(sqlstr)
    rs = cur.fetchall()
    for r in rs:
        print(r)

    cur.close()

def search_record(eno):
    global con 
    sqlstr = 'select *from emp where empid = %s'
    cur = con.cursor()
    cur.execute(sqlstr, (eno,))
    rs = cur.fetchone()
    print(rs)
    cur.close()

def update_record(eno, ena, sal):
    global con 
    sqlstr = 'update emp set ename = %s, salary = %s where empid=%s'
    cur = con.cursor()
    cur.execute(sqlstr, (ena, sal, eno))
    con.commit()
    cur.close()
    print('One Record is updated successfully')

def delete_record(eno):
    global con
    sqlstr = 'delete from emp where empid = %s'
    cur = con.cursor()
    cur.execute(sqlstr, (eno,))
    print('One Record is deleted successfully')
    cur.close()
    

if __name__ == '__main__':
    while True:
        print('1. Add Record')
        print('2. Show Records' )
        print('3. Search Record')
        print('4. Update Record')
        print('5. Delete Record')
        print('6. Exit')
        choice = int(input('Enter Your chocice [1-6] : '))

        if choice == 1:
            eno = int(input('Enter Employee Number : '))
            ena = input('Enter Employee Name : ')
            sal = float(input('Enter Employee Salary  : '))
            add_record(eno, ena, sal)

        elif choice ==2: 
            show_all()
        elif choice==3:
            eno = int(input('Enter Employee Number to search : '))
            search_record(eno)

        elif choice == 4:
            eno = int(input('Enter Empoyee Nuber to update : '))
            ena = input('Enter New Employee Name : ')
            sal = float(input('Enter New Employee Salary : '))
            update_record(eno, ena, sal)

        elif choice==5:
            eno = int(input('Enter Employee Number to delete : '))
            delete_record(eno)

        elif choice==6:
            global con 
            con.close()
            break
        else:
            print('Invalid choice, try again....')