# coding: utf-8
#

import hashlib


def hashmd5(handler, s):
    return hashlib.md5(s).hexdigest()