#!/usr/bin/python  
# -*- coding: utf-8 -*-  

from __future__ import print_function

import os

import fire
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.websocket
from tornado.log import enable_pretty_logging

from settings import COOKIE_SECRET
import handlers.page
import handlers.api


def make_app(**settings):
    settings['template_path'] = 'templates'
    settings['static_path'] = 'static'
    settings['cookie_secret'] = 'SECRET:_'+COOKIE_SECRET
    settings['login_url'] = '/login'
    settings['websocket_ping_interval'] = 15
    return tornado.web.Application([
        (r"/", handlers.page.MainHandler),
        (r"/login", handlers.page.LoginHandler),
        (r"/logout", handlers.page.LogoutHandler),
        (r"/api/v1/user", handlers.api.APIUserHandler),
    ], **settings)


def main(debug=False, port=4000):
    enable_pretty_logging()
    app = make_app(debug=debug)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    try:
        print("Listen on port {}".format(port))
        http_server.listen(port)
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print("Try to stop server")
        tornado.ioloop.IOLoop.instance().stop()


if __name__ == "__main__":
    fire.Fire(main)