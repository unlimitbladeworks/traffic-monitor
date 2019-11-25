# -*- coding: utf-8 -*-
"""
@Author  : Sy
@File    : hello.py
@Time    : 2019-11-17 10:52
@desc    :
"""
from . import web


@web.route('/hello')
def index():
    return 'hello world'
