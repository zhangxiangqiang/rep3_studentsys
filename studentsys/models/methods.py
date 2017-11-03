# coding: utf8
from db import conn, cur

# 读数据用的函数


# 查询用户
def select_email(email):
    sql = "select * from users where email= %s"
    cur.execute(sql,(email,))
    lines = cur.fetchall()
    return lines


# 取字段
def select_columns(table, column):
    sql = "select " + column + " from " + table
    cur.execute(sql)
    lines = cur.fetchall()
    return lines


# 取出全部对象
def select_all(table):
    from db import conn, cur
    sql = "select * from " + table
    cur.execute(sql)
    conn.commit()
    lines = cur.fetchall()
    return lines


# 保存用户信息
def save_users(email, password):
    sql = "insert into users(email, password)VALUES(%s, %s)" % (email, password)
    cur.execute(sql)
    conn.commit()


# 保存学生信息
def save_student(student_name, point, major, student_class, age):
    sql = """
         insert into students(student_name, point, major, student_class, age)
         VALUES(%s, %s,%s,%s,%s);
         """


    cur.execute(sql, (student_name, point, major, student_class, age))
    conn.commit()


#删除学生信息
def del_student(id):
    sql = "delete from students where id=%s"
    cur.execute(sql,(id,))
    conn.commit()








