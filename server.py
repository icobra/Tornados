# coding: utf8
# version 0.00001

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os.path

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/about", AboutHandler),
            (r"/faq", FaqHandler),
            (r"/test", TestHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html",
            page_title = "Tornados главная",
            header_text = "Мы рады вам",
        )

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "about.html",
             page_title = "О нас",
             header_text = "Мы работаем с 2008 года",
        )

class FaqHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Fast answers and questions")

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "test.html",
            page_title = "Test",
            header_text = "Проверка функционала",
        )

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
