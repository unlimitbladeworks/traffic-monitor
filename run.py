# -*- coding: utf-8 -*-
"""
@Author  : Sy
@File    : run.py
@Time    : 2019-11-17 10:44
@desc    : flask 启动脚本
"""

from app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
