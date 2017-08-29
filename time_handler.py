#coding=utf-8
from dateutil import tz  
import datetime,time
  
def utc2local(utc_st):
    # “”“UTC时间转本地时间（+8:00）”“”
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    print offset
    local_st = utc_st + offset
    return local_st
utc_time = datetime.datetime(2014, 9, 18, 10, 42, 16, 126000)
a = utc2local(utc_time)
print a