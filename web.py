#!/usr/bin/python  
# -*- coding: utf-8 -*-  

import os

import fire
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.websocket
from tornado.log import enable_pretty_logging

import handlers.page

enable_pretty_logging()


def make_app(**settings):
    settings['template_path'] = 'templates'
    settings['static_path'] = 'static'
    settings['cookie_secret'] = 'SECRET:_'+os.environ.get("SECRET", "")
    settings['login_url'] = '/login'
    settings['websocket_ping_interval'] = 15
    return tornado.web.Application([
        (r"/", handlers.page.MainHandler),
    ], **settings)


def main(debug=False, port=4000):
    app = make_app(debug=debug)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    try:
        http_server.listen(port)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("Try to stop server")
        tornado.ioloop.IOLoop.instance().stop()


if __name__ == "__main__":
    fire.Fire(main)