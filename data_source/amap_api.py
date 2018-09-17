# coding = utf-8

"""
@author: sy

@file: amap_api.py

@time: 2018/6/3 18:59

@desc: 高德地图API的信息类

用到的官方API:

    http://lbs.amap.com/api/webservice/gettingstarted 申请key值

    http://lbs.amap.com/api/webservice/guide/api/georegeo#geo 地理编码

    http://lbs.amap.com/api/webservice/guide/api/trafficstatus#road 指定线路交通态势

"""

import requests
from requests import RequestException
import json

# 获取地图信息类
from utils import util


class ReadMapInfo:
    # 初始化key
    def __init__(self):
        self.key = util.read_key()

    # 请求url方法get方法
    def request_url_get(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        try:
            r = requests.get(url=url, headers=headers, timeout=30)
            if r.status_code == 200:
                return r.text
            return None
        except RequestException:
            print('请求url返回错误异常')
            return None

    # 请求url方法post方法
    def request_url_post(self, url, data):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        try:
            r = requests.post(url=url, headers=headers, data=data, timeout=30)
            if r.status_code == 200:
                return r.text
            return None
        except RequestException:
            print('请求url返回错误异常')
            return None

    # 获取地理编码方法(adcode, location),args:城市、具体路段
    def read_geo(self, city, address):
        """ 请求地理编码的url地址 """
        url = f'https://restapi.amap.com/v3/geocode/geo?city={city}&address={address}&&key={self.key}'
        r = self.request_url_get(url)
        result_json = self.parse_json(r)
        # 如果请求成功则进行处理,否则返回空,获取城市标识
        if result_json['status'] == '1':
            geocodes_list = list(result_json['geocodes'])
            geocodes_json = geocodes_list.pop()
            adcode = geocodes_json['adcode']
            location = geocodes_json['location']
            return adcode, location
        else:
            return None

    # 获取指定路线交通趋势,道路模式默认矩形
    def read_road(self, city, address, **kwargs):
        """ 必传参数: 城市,地址,用户key;
            可选参数: select_road_mode(交通趋势)
                        1.rectangle (矩形区域交通态势)
                        2.circle    (圆形区域交通态势)
                        3.road      (指定路线交通态势) ***此方式貌似有Bug(待解决)***
        """
        for arg_name in kwargs:
            setattr(self, arg_name, kwargs[arg_name])

        """ 若有参数传入,则选择客户端的参数,否则默认矩形区域交通态势 """
        if kwargs['select_road_mode']:
            select_road_mode = kwargs['select_road_mode']
        else:
            select_road_mode = 'road'

        adcode, location = self.read_geo(city, address)
        """ 根据客户端传入的标识选择不同的道路模式:rectangle(矩形),circle(圆形),road(指定路线)"""
        if select_road_mode == 'rectangle':
            """ 矩形的坐标入参,规则:左下右上顶点坐标对。() """
            if kwargs['rectangle']:
                rectangle = kwargs['rectangle']
            else:
                print(
                    '既然选择了矩形区域交通态势,就必须传入rectangle参数!\n'
                    '写法为:左下右上顶点坐标对。\n'
                    '      矩形对角线不能超过10公里两个坐标对之间用”;”\n'
                    '      间隔xy之间用”,”间隔!\n'
                    '例如:(116.351147,39.966309;116.357134,39.968727)')
            # 矩形url查询经度和纬度使用","分隔坐标之间使用";"分隔.例如：x1,y1;x2,y2
            url = f'https://restapi.amap.com/v3/traffic/status/rectangle?rectangle={rectangle}&key={self.key}'
        if select_road_mode == 'circle':
            # 半径参数默认1000m
            url = f'https://restapi.amap.com/v3/traffic/status/circle?location={location}&key={self.key}'
        if select_road_mode == 'road':
            # 请求指定路线交通趋势的url地址
            url = f'https://restapi.amap.com/v3/traffic/status/road?name={address}&adcode={adcode}&key={self.key}'
        r = self.request_url_get(url)
        print(r)

    # 通过拾取器获取详细的坐标,通过关键词进行搜索,返回具体详细坐标
    def read_picker(self, city, keyword='天安门'):
        # 获取城市的编码
        city_adcode_json = util.read_city_adcode().replace('\n', '').replace('\t', '')
        result_city_adcode_json = self.parse_json(city_adcode_json)
        cities_list = result_city_adcode_json['cities']
        for city_dict in cities_list:
            if city in city_dict.values():
                city_adcode = city_dict['adcode']
        # POI 查询(关键词搜索)
        url = f'https://restapi.amap.com/v3/place/text?keywords={keyword}&city={city_adcode}&key={self.key}&extensions=all'
        poi_json = self.request_url_get(url)
        result_json = self.parse_json(poi_json)
        pois = result_json['pois']
        for path_detail in pois:
            print('ID:' + path_detail['id'] + ',name:' + path_detail['name'] + ';')
        id_1 = input('请选择您要输入的起始位置id:\n')
        id_2 = input('请选择您要输入的终止位置id:\n')
        for path_detail in pois:
            if id_1 == path_detail['id']:
                location_1 = path_detail['location']
            if id_2 in path_detail['id']:
                location_2 = path_detail['location']
        try:
            location_tuple = (location_1,location_2)
            return location_tuple
        except Exception as e:
            print ('您输入的两次ID有误!请检查!错误:',e)
        pass
    # 解析json函数
    def parse_json(self, content_json):
        result_json = json.loads(content_json)
        return result_json


if __name__ == '__main__':
    readMapInfo = ReadMapInfo()
    readMapInfo.read_picker('北京市', keyword='天安门')
