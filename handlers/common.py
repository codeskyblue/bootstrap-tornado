#!/usr/bin/python  
# -*- coding: utf-8 -*-

import json
import tornado.web
from tornado import gen

from database import db


class BaseHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def prepare(self):
        user_id = self.get_secure_cookie("user_id")
        if not user_id:
            return
        self.current_user = yield db.get_user(user_id)

    def write_json(self, data):
        """ Support datetime json dumps """
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.write(json.dumps(data, default=self._date_handler))
    
    def _date_handler(self, obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj