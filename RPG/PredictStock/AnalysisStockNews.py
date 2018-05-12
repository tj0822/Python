#-*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates

output = pd.read_csv('output/output_2017-01-01~2017-08-10.csv')

# byStockName = output.groupby('name')

# print(byStockName['name'].describe())


# print(output[output['name'] == '카카오'])

# print(list(output['date']))
# print(list(output['count']))

# plt.plot_date(['2017-01-01', '2017-01-02', '2017-01-03'], [4, 5, 6])
# plt.show()

stockName = '삼성전자'

new_date = dates.datestr2num(list(output[output['name'] == stockName]['date']))

plt.plot_date(new_date, list(output[output['name'] == stockName]['count']))
plt.ylabel('Number of count')
plt.show()