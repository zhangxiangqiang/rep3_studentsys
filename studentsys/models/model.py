# coding: utf8

from methods import conn, cur

# 数据表创建文件，若要创建新表，请在创建后运行此文件


class Table(object):
    # 用户表
    def create_users(self):
        cur.execute('''CREATE TABLE IF NOT EXISTS users(
               id SERIAL PRIMARY KEY     NOT NULL,
               username          VARCHAR(10)    ,
               email         VARCHAR(15)   NOT NULL,
               password      VARCHAR(10)  NOT NULL,
               age            INT     );''')


    #  学生表
    def create_students(self):
        cur.execute('''CREATE TABLE IF NOT EXISTS students
               (id  SERIAL PRIMARY KEY     NOT NULL,
               student_name   VARCHAR(10)    NOT NULL,
               point          REAL   NOT NULL,
               major          VARCHAR(10)  NOT NULL,
               student_class          CHAR(10)  NOT NULL,
               age            INT     NOT NULL);''')


if __name__ == "__main__":
    table = Table()
    table.create_users()
    table.create_students()
    conn.commit()
    conn.close()



