traffic-monitor(基于高德地图的交通数据分析)
===
[![Python](https://img.shields.io/badge/python-v3.6+%2B-blue.svg)](https://www.python.org/)
[![build](https://img.shields.io/badge/build-passing-green.svg)](https://github.com/unlimitbladeworks/sy-pynotebook)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)



设计需求在于每天上班早高峰期,每次都提前出门,虽然有地图可以实时查看路况,但是再过一阵时间
就会异常的堵车如果通过数据监控分析每天指定路段在什么时间段相应的拥堵情况,即可合理控制时间.
有时候很早出门,却堵车堵得依然快迟到,而有时出门时间晚了,却发现那个时间段的路况良好,和早出门最终到达目的地的时间相近。

![amap](https://github.com/unlimitbladeworks/traffic-monitor/raw/master/picture/map.png "高德地图样照")

Environment(环境)
---
本项目为python编写的项目。

- python3.6+

安装用到的库:

```
pip install -r requirements.txt 
```

requirements 中涉及到的 gunicorn、gevent ：用于后续 web 部署。 

PS: 如果安装依赖库慢，将自己的 pip 源改为国内镜像即可。

<hr>

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

4.搜索POI:

[https://lbs.amap.com/api/webservice/guide/api/search](https://lbs.amap.com/api/webservice/guide/api/search)

5.地图拾取器(网页,可以手工处理,也可用python调用获取返回值):

网页:
[https://lbs.amap.com/console/show/picker](https://lbs.amap.com/console/show/picker)

F12后台请求地址（实际上就是请求的POI搜索）:
https://restapi.amap.com/v3/place/text

<hr>

详情参考之前写过的文章：

- [Python玩转高德地图API（一）](https://mp.weixin.qq.com/s/7Ktv-cYNNT82ECVGevUyzg)
- [Python玩转高德地图API（二）](https://mp.weixin.qq.com/s/8rOBebnJxQZ3qBPUVmrGqg)

运行使用
---


由于结构目录已调整，有想在原有基础修改源码的同学，可以打开 app 目录下的 old_run.py 即可运行。



Todo List
---

修改了原有代码结构。

- [ ] 重构代码迁移到 flask 项目上
    - [x] 改为 flask 项目结构
    - [ ] 新增前端页面
    - [x] 原 run.py 改动 flask 启动脚本, 现 old_run.py 改为业务模块脚本
    - [ ] 迁移现有的目录结构到新结构上
    
- [ ] 持续完善 markdown 文档
    - [ ] 待完善