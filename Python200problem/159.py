#-*- coding:utf-8 -*-

from time import localtime
weekdays = ['월', '화', '수', '목', '금', '토', '일']

t = localtime()
today = '%d-%d-%d' %(t.tm_year, t.tm_mon, t.tm_mday)
week = weekdays[t.tm_wday]

print('오늘(%s)은 %s요일 입니다.' %(today, week))
