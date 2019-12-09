# -*- coding: utf-8 -*-
"""
@Author  : Sy
@File    : __init__.py.py
@Time    : 2019-11-25 09:42
@desc    : 初始化 app 应用
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 注册蓝图
    register_blueprint(app)
    return app


# 注册蓝图
def register_blueprint(app):
    # 注册 web 的蓝图
    from app.web import web
    app.register_blueprint(web)


def test():
    pass