#!/usr/bin/python  
# -*- coding: utf-8 -*-

from .common import BaseHandler


class MainHandler(BaseHandler):
    def get(self):
        self.render('index.html')