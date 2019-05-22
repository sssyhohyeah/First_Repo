'''
    数据库读操作演示（查找select）
'''

import os

import pymysql

db = pymysql.connect(host="localhost",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8"
                     )

c = db.cursor()

sql = "select * from myclass where age=13;"

c.execute(sql)

print(c.fetchone())
print()
print(c.fetchmany(3))
print()

# c.execute(sql)
print(c.fetchall())
print()
print(c.fetchone())

db.close()

print()
print()
