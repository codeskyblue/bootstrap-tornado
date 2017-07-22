# coding: utf-8

import os

PORT = int(os.environ.get("PORT", 4000))

RDB_HOST = os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015
RDB_NAME = os.environ.get('RDB_NAME') or 'bootstrap-tornado'