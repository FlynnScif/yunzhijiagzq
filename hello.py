#-*- coding:utf-8 -*-
import web
from web.contrib.template import render_jinja #web.py对调用jinja2的模块

urls = ("/","hello",
        )



render = render_jinja(
    'templates',#模板存放的目录名
    encoding = 'utf-8',#模板使用的编码
    )

class hello:#class hello(object)有什么区别 
    def GET(self):
        return render.index()       # return "hello world"

if __name__ == "__main__":
    app = web.application(urls,globals())
    app.run()