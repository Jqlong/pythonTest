from datetime import date, time, datetime, timedelta


today = date.today()
print("Output 1:today:{0!s}".format(today))  # !s：转换成字符串
print(type(today))
print("Output 2:year:{0!s}".format(today.year))
print("Output 3:year:{0!s}".format(today.month))
print("Output 4:year:{0!s}".format(today.day))
current_time = datetime.today()
print("Output 4:year:{0!s}".format(current_time))  # 获取当前的时间，精确到秒

# 使用timedelta计算一个新日期
one_day = timedelta(days=-1)  # 从今天减去1天
yesterday = today + one_day
print("Output 5:{0!s}".format(yesterday))  # 减一天

date_diff = today - yesterday
print("Output 6:{0!s}".format(date_diff))



