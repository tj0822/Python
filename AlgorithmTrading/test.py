#-*- coding:utf-8 -*-

import math
import datetime
import pandas as pd

date = '2017-01-01'
yesterday = datetime.datetime.today() + datetime.timedelta(days=-1)
print(pd.to_datetime(date + ' 15:30:00') + datetime.timedelta(days=-1))
print(pd.to_datetime(date + ' 15:30:00'))

print(pd.to_datetime(date + ' 15:30:30'))
print(type(date))
print(type(pd.to_datetime(date + ' 15:30:30')))