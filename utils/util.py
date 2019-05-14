# coding = utf-8

"""
@author: sy

@file: util.py

@time: 2018/8/26 11:01

@desc: 工具类

"""
import os


# 持久化key,便于读取
def read_key():
    # 获取key文件的绝对路径
    key_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'key')
    with open(key_path, 'r', encoding='utf-8') as f:
        key = f.read()
    return key


def read_city_adcode():
    city_adcode_path = os.path.join(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'geography_json'), 'city_adcode_json')
    with open(city_adcode_path, 'r', encoding='utf-8') as f:
        city_adcode_json = f.read()
        f.close()
    return city_adcode_json
