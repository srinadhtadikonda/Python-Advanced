import pymysql
try:
    con = pymysql.connect(host='localhost',
                          user='root',
                          password='root123',
                          database='demo')
    print('Database is connected')
    con.close()
except pymysql.Error as e:
    print(f'Error : {e}')
