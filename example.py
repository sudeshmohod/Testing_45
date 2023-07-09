import psycopg2 as pg
conn=pg.connect(user='postgres',
                password='sudesh',
                host='127.0.0.1',
                port='5432')
conn.autocommit=True
cursor1=conn.cursor()
sql='''create database "testing-45" '''
cursor1.execute(sql)
print('database created')