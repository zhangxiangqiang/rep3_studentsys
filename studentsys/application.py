# coding: utf8

from url import url
import tornado.web
import os

# 网站系统基本配置
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",  #将cookie 值编码为 Base-64 字符串
    xsrf_cookies=True,  # 开启 XSRF 保护
    login_url='/',   # 如果用户不合法，根据这个设置，会返回到首页
    debug=False,
)


# 请求处理集合
application = tornado.web.Application(
    handlers=url,
    **settings
)