# coding = utf-8

"""
@author: sy

@file: amap_api.py

@time: 2018/6/3 18:59

@desc: 高德地图英文名称

用到的官方API:

    http://lbs.amap.com/api/webservice/gettingstarted 申请key值

    http://lbs.amap.com/api/webservice/guide/api/georegeo#geo 地理编码

    http://lbs.amap.com/api/webservice/guide/api/trafficstatus#road 指定线路交通态势

"""

import requests
from requests import RequestException
import json


# 获取地图信息类
class ReadMapInfo:
    # 请求url方法
    def request_url(self, url):
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        try:
            r = requests.get(url=url, headers=headers)
            if r.status_code == 200:
                return r.text
            return None
        except RequestException:
            print('请求url返回错误异常')
            return None

    # 获取地理编码方法,args:城市、具体路段、开发者key
    def read_geo(self, city, address, key):
        """ 请求地理编码的url地址 """
        url = f'https://restapi.amap.com/v3/geocode/geo?city={city}&address={address}&&key={key}'
        r = self.request_url(url)
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
    def read_road(self, city, address, key, **kwargs):
        """ 必传参数: 城市,地址,用户key;
            可选参数: select_road_mode(交通趋势)
                        1.rectangle (矩形区域交通态势)
                        2.circle    (圆形区域交通态势)
                        3.road      (指定路线交通态势) ***此方式貌似有Bug(待解决)***
        """
        for key in kwargs:
            setattr(key, kwargs[key])

        select_road_mode = kwargs['select_road_mode']
        adcode, location = self.read_geo(city, address, key)
        """ 根据客户端传入的标识选择不同的道路模式:rectangle(矩形),circle(圆形),road(指定路线)"""
        if select_road_mode == 'rectangle':
            # 矩形url查询经度和纬度使用","分隔坐标之间使用";"分隔.例如：x1,y1;x2,y2
            url = f'https://restapi.amap.com/v3/traffic/status/rectangle?rectangle={rectangle}&key={key}'
        if select_road_mode == 'circle':
            # 半径参数默认1000m
            url = f'https://restapi.amap.com/v3/traffic/status/circle?location={location}&key={key}'
        if select_road_mode == 'road':
            # 请求指定路线交通趋势的url地址
            url = f'https://restapi.amap.com/v3/traffic/status/road?name={address}&adcode={adcode}&level={level}&key={key}'
        r = self.request_url(url)
        print(r)

    # 解析json函数
    def parse_json(self, content_json):
        result_json = json.loads(content_json)
        return result_json


if __name__ == '__main__':
    readMapInfo = ReadMapInfo()
    readMapInfo.read_road('北京', '管庄路', '439b13eba868071ba3d294a07c2bc573', select_road_mode='road', level=6)
    readMapInfo.read_road('北京', '管庄路', '439b13eba868071ba3d294a07c2bc573')
