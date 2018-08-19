#coding = utf-8

"""
@author: sy

@file: amap_api.py

@time: 2018/6/3 18:59

@desc: 高德地图英文名称

    http://lbs.amap.com/api/webservice/gettingstarted 申请key值

    http://lbs.amap.com/api/webservice/guide/api/georegeo#geo 地理编码

    http://lbs.amap.com/api/webservice/guide/api/trafficstatus#road 指定线路交通态势

"""

import requests
from requests import RequestException


class ReadMapInfo:

    #请求url方法
    def request_url(self,url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        try:
            r = requests.get(url=url,headers=headers)
            if r.status_code == 200:
                return r.text
            return None
        except RequestException:
            print('请求url返回错误异常')
            return None


    #获取地理编码方法
    def read_geo(self):
        pass


    #获取指定路线交通趋势
    def read_road(self):
        pass



