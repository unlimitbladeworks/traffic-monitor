# coding = utf-8

"""
@author: sy

@file: util.py

@time: 2018/8/26 11:01

@desc: 工具类

"""
import os


def read_key():
    """ 持久化key,便于读取 """
    # 获取key文件的绝对路径
    key_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'user_key')
    with open(key_path, 'r', encoding='utf-8') as f:
        key = f.read()
    return key


def read_city_adcode():
    """ 读取本地城市 json 码 """
    city_adcode_path = os.path.join(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'geography_json'), 'city_adcode_json')
    with open(city_adcode_path, 'r', encoding='utf-8') as f:
        city_adcode_json = f.read()
    return city_adcode_json


if __name__ == '__main__':
    print(read_city_adcode())
    print(read_key())
