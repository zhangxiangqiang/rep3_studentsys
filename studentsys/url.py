# coding: utf8

'''
路由
'''

import sys
reload(sys)

from handlers.index import IndexHandler, RegisterHandler
from handlers.student_admin import StudentHandler, AddStudentHandler, DelStudentHandler

url = [
    (r'/', IndexHandler),
    (r'/register', RegisterHandler),
    (r'/student_list', StudentHandler),
    (r'/add_student', AddStudentHandler),
    (r'/del_student', DelStudentHandler),

]
