# -*- coding: utf-8 -*-
"""
@Author  : Sy
@File    : __init__.py.py
@Time    : 2019-11-17 10:40
@desc    : 蓝图初始化操作
"""

from flask import Blueprint, render_template

web = Blueprint('web', __name__)


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html')


from . import index
