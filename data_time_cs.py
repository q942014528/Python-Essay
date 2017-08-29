#coding=utf-8
import datetime,re
def handler_time(y,m,d):
    """
    给日期求天数
    """
    targetDay = datetime.date(y, m, d)  #将输入的日期格式化成标准的日期
    print targetDay.year-1,12,31
    print datetime.date(targetDay.year - 1, 12, 31)
    dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  #减去上一年最后一天
    print('%s是%s年的第%s天。'% (targetDay, y, dayCount.days))


if __name__=="__main__":

    time = "2017-01-01"
    time = re.findall("(\d{4}).*?(\d{2}).*?(\d{2})",time)
    year,month,day = int(time[0][0]),int(time[0][1]),int(time[0][2])
    handler_time(year,month,day)