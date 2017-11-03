# coding: utf8
from models.methods import save_student, del_student
import tornado.web
from models.methods import select_all
from base import BaseHandler



class StudentHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        students = select_all("students")
        email = self.get_current_user()
        self.render("student_list.html", students=students, email=email)


class AddStudentHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("add_student.html")

    def post(self):
        student_name = self.get_argument("student_name")
        point = self.get_argument("point")
        major = self.get_argument("major")
        student_class = self.get_argument("student_class")
        age = self.get_argument("age")
        save_student(student_name, point, major, student_class, age)
        self.redirect('/student_list')


class DelStudentHandler(BaseHandler):
    def post(self):
        id = self.get_argument("id")
        del_student(id)
        self.redirect('/student_list')




