# -*- coding: utf-8 -*-
"""
@Author  : Sy
@File    : index.py
@Time    : 2019-11-17 10:52
@desc    :
"""
from flask import render_template
from . import web
from app import mongo


@web.route('/hello')
def hello():
    result = mongo.db.traffic.find()  # 文档插入集合
    result_list = str([el for el in result])
    return result_list


@web.route('/index')
def index():
    return render_template('index.html')
