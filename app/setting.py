# -*- coding: utf-8 -*-
"""
@Author  : Sy
@File    : setting.py
@Time    : 2019-12-09 10:41
@desc    :
"""
HOST = "0.0.0.0"  # flask 主机
PORT = 8888  # flask 端口
DEBUG = True  # 是否debug模式
# mongodb://数据库用户名:数据库密码@ip:port/库名 ; 若无数据库登录验证，改为 "mongodb://127.0.0.1:27017/traffic"
MONGO_URI = "mongodb://user:password@127.0.0.1:27017/traffic"
