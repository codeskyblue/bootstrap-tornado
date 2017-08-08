#!/usr/bin/python  
# -*- coding: utf-8 -*-

from __future__ import print_function

import base64
import tornado.web
from tornado import gen

from .common import BaseHandler
from auth.openid import OpenIdMixin
from database import db



# URL: /login
class LoginHandler(tornado.web.RequestHandler, OpenIdMixin):
    # Change to your company OpenID url
    _OPENID_ENDPOINT = base64.b64decode('aHR0cHM6Ly9sb2dpbi5uZXRlYXNlLmNvbS9vcGVuaWQv')

    @gen.coroutine
    def _openid_callback(self, user):
        if user is None:
            self.write("check auth failed, need login again")
            self.finish()
        else:
            user['ip'] = self.request.remote_ip
            email = yield db.save_user(user)

            self.set_secure_cookie("user_id", email)
            next_url = self.get_argument("next", "/")
            self.redirect(next_url)

    @tornado.web.asynchronous
    def get(self):
        """"
        Support two type login, openid and TOP(jwt)
        """
        # check callback
        if self.get_argument('openid.mode', False):
            self.get_authenticated_user(self._openid_callback)
            return
        
         # redirect to login
        next_url = self.get_argument("next", "/")
        self.authenticate_redirect()


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("user_id")
        next_url = self.get_argument("next", "/")
        self.redirect(next_url)


class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')