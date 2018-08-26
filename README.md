traffic-monitor(基于高德地图的交通数据分析)
===

设计需求在于每天上班早高峰期,每次都提前出门,虽然有地图可以实时查看路况,但是再过一阵时间
就会异常的堵车如果通过数据监控分析每天指定路段在什么时间段相应的拥堵情况,即可合理控制时间.
有时候很早出门,却堵车堵得依然快迟到,而有时出门时间晚了,却发现那个时间段的路况良好,和早出门最终到达目的地的时间相近。

![amap](https://github.com/unlimitbladeworks/traffic-monitor/raw/master/picture/map.png "高德地图样照")

Environment(环境)
---
本项目为python编写的项目。

- python3.6+

用到的库:

- requests
- json

coding之前的准备工作:

- 登录高德地图官网,申请相关账号
- 参考下面的高德API网址申请key值

Amap(高德地图)API网址
---
1.申请key值:

[http://lbs.amap.com/api/webservice/gettingstarted](http://lbs.amap.com/api/webservice/gettingstarted)

2.地理编码:

[http://lbs.amap.com/api/webservice/guide/api/georegeo#geo](http://lbs.amap.com/api/webservice/guide/api/georegeo#geo)

3.指定线路交通态势:

[http://lbs.amap.com/api/webservice/guide/api/trafficstatus#road](http://lbs.amap.com/api/webservice/guide/api/trafficstatus#road)

4.地图拾取器(网页,可以手工处理,也可用python调用获取返回值):

网页:
[https://lbs.amap.com/console/show/picker](https://lbs.amap.com/console/show/picker)

F12后台请求地址:
https://restapi.amap.com/v3/place/text
