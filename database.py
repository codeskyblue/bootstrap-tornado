#!/usr/bin/python  
# -*- coding: utf-8 -*-
# reference:
#    https://github.com/openstf/stf/blob/master/lib/db/tables.js
#    https://github.com/openstf/stf/blob/master/lib/db/api.js

import uuid
import datetime
import os
import functools
from collections import defaultdict

import rethinkdb as r
from tornado import gen
from tornado import ioloop

import utils
from settings import *


def setup():
    conn = r.connect(host=RDB_HOST, port=RDB_PORT)

    def safe_run(rql):
        try:
            rql.run(conn)
        except r.RqlRuntimeError:
            pass

    safe_run(r.db_create(RDB_NAME))
    safe_run(r.db(RDB_NAME).table("users").index_create("token"))
    print 'Database init success'
    conn.close()


setup()
r.set_loop_type("tornado")

def time_now():
    return datetime.datetime.now(r.make_timezone('+08:00'))


class DB(object):
    @gen.coroutine
    def run(self, oper):
        conn = yield r.connect(host=RDB_HOST, port=RDB_PORT, db=RDB_NAME)
        try:
            ret = yield oper.run(conn)
            raise gen.Return(ret)
        finally:
            conn.close()
    
    @gen.coroutine
    def drop_database(self):
        yield self.run(r.db_drop(RDB_NAME))
    
    @gen.coroutine
    def get_user(self, email):
        user = yield self.run(r.table("users").get(email))
        raise gen.Return(user)
    
    @gen.coroutine
    def save_user(self, user):
        """
        Return:
            - email(string): user id
        """
        ret = yield self.run(r.table("users").get(user['email']).update({
            "name": user['name'],
            "lastLoggedInAt": time_now(),
        }))
        if ret['skipped']:
            yield self.run(r.table("users").insert({
                "email": user['email'],
                'name': user['name'],
                'lastLoggedInAt': time_now(),
                'createdAt': time_now(),
            }))
        raise gen.Return(user['email'])


db = DB()
