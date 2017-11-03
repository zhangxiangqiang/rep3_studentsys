# coding: utf8
import psycopg2

conn = psycopg2.connect(database='studentsys', user='postgres', password='qing'
                        , host='127.0.0.1',port='5432')   #连接对象
cur = conn.cursor()  #游标对象