# -*- coding: utf-8 -*-
"""
@author: sy

@file: run.py

@time: 2018年08月21日23:04:01

@desc: traffic-monitor main function

"""
import os
import sys

from data_source.amap_api import ReadMapInfo
from apscheduler.schedulers.blocking import BlockingScheduler

""" 加载包变量 """
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_PATH)


# 手工处理,人工介入的定时任务
def hand_job():
    readMapInfo = ReadMapInfo()
    location_tuple = readMapInfo.read_picker('北京市', '西长安街')
    if location_tuple:
        left_loaction = location_tuple[0]
        right_loaction = location_tuple[1]
        rectangle = left_loaction + ';' + right_loaction
    readMapInfo.read_road('北京市', '西长安街', select_road_mode='rectangle', rectangle=rectangle)


def my_job():
    print('hello world!')


# 入口函数
def main():
    # 基于quartz的定时任务调度器
    scheduler = BlockingScheduler()
    """ FIELD_NAMES = ('year', 'month', 'day', 'week', 'day_of_week', 'hour', 'minute', 'second') """
    scheduler.add_job(my_job, 'cron', second='0/2', id='my_job_id')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.remove_job('my_job_id')


if __name__ == '__main__':
    main()
