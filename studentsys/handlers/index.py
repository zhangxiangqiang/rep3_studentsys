# coding: utf8

import tornado.web
from models import methods
from base import BaseHandler
import tornado.escape


# 登录
class IndexHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        email = self.get_argument("email") #接收前端传过来的数据
        password = self.get_argument("password")
        user_infos = methods.select_email(email=email)
        if user_infos:
            db_pwd = user_infos[0][3]
            if db_pwd == password:
                # self.set_secure_cookie(username, db_pwd)   # 设置cookie
                self.set_current_user(email)   # #将当前用户写入 cookie
                self.redirect("/student_list")
            else:
                self.write("密码错误")
        else:
            self.write("您还没有注册呢")


# 注册
class RegisterHandler(BaseHandler):
    def get(self):
        self.render("register.html")

    def post(self):
        email = self.get_argument('email')
        password1 = self.get_argument('password1')
        password2 = self.get_argument('password2')
        user_infos = methods.select_email(email=email)
        if user_infos:
            self.write('此邮箱已经存在，请直接登录')
        else:
            if password1 != password2 or not password1:
                self.write('密码不一致，请重新输入')
            if not email:
                self.write('邮箱不能为空')
            else:
                methods.save_users(email, password1)
                self.render('login.html')





class ErrorHandler(BaseHandler):
    """处理访问错误"""
    def get(self):
        self.render("error.html")


