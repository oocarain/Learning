#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

import pymysql

db = pymysql.connect('localhost','oocarain','123456','pytest')
cursor = db.cursor()
sql = """create table shan(id int(11) primary key,
        name varchar(25),
        salary float)"""

         #('qian','c',25,'M',2035),
         #('su','d',23,'M',1756)"""

try:
    #执行sql语句
    cursor.execute(sql)
    #提交到数据库
    db.commit()
except:
    #发生错误则回滚
    db.rollback()

db.close()
print('----success----')
