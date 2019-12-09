# -*- coding: utf-8 -*-
"""
@Author  : Sy
@File    : hello.py
@Time    : 2019-11-17 10:52
@desc    :
"""
from flask import render_template

from . import web


@web.route('/hello')
def hello():
    return 'hello world'


@web.route('/index')
def index():
    return render_template('index.html')
