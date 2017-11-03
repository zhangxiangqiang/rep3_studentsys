# coding: utf8

import tornado.ioloop  # 实现非阻塞 socket 循环
import tornado.options  # 命令行解析模块
import tornado.httpserver  # 这个模块就是用来解决 web 服务器的 http 协议问题,实现客户端和服务器端的互通

from application import application

from tornado.options import define, options

# 项目启动文件

# 定义访问本服务器的端口,
define("port", default=8080, help="run on the given port", type=int)


def main():
    tornado.options.parse_command_line()
    #  建立http 服务
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)

    print "Development server is running on http://127.0.0.1:%s" % options.port
    print "Quit the server with Control-C"
    # 接收来自 HTTP 的请求
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
