# coding: utf-8
#

from __future__ import print_function

import base64
import tornado.web
from tornado import gen
from database import db
from .common import BaseHandler


class APIUserHandler(BaseHandler):
    @gen.coroutine
    def get(self):
        user_id = self.get_secure_cookie("user_id")
        user = None
        if user_id:
            user = yield db.get_user(user_id)
        
        if not user:
            self.write({
                "success": False,
                "description": "user is not logged in"
            })
        else:
            self.write_json({
                "success": True,
                "value": user,
            })
