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
        if self.current_user:
            self.write_json({
                "success": True,
                "value": self.current_user,
            })
        else:
            self.write({
                "success": False,
                "description": "user is not logged in"
            })
