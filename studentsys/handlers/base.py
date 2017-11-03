# coding: utf8

import tornado.web
import tornado.escape


class BaseHandler(tornado.web.RequestHandler):
    """得到当前的 cookie"""
    def get_current_user(self):
        return self.get_secure_cookie("email")

    def set_current_user(self, email):
        if email:
            self.set_secure_cookie('email', tornado.escape.json_encode(email))  # email 转化为 json，写入到了 cookie
        else:
            self.clear_cookie(email)


