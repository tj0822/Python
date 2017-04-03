#-*- coding:utf-8 -*-

import pandas as pd
import csv

fileName = '가격정보(035720_카카오)_enc.csv'


stockData = open(fileName, 'r', encoding='utf-8')
reader = csv.reader(stockData)
stockList = list(reader)
df = pd.DataFrame(stockList[1:])
print(stockList[0])
df.columns = stockList[0]
# print(df.columns)
# print(int(df['종가'][0].replace(',', '')))

# print(pd.Series(df['종가'].str.replace(',', '')).astype(int))


# for i in range(0, df.__len__()):
#     print(df['날짜'][i], ' : ', int(str(df['시가'][i]).replace(',','')))

df['종가'] = pd.Series(df['종가'].str.replace(',', '')).astype(int)
df['시가'] = pd.Series(df['시가'].str.replace(',', '')).astype(int)
df['고가'] = pd.Series(df['고가'].str.replace(',', '')).astype(int)
df['저가'] = pd.Series(df['저가'].str.replace(',', '')).astype(int)
# df['거래량'] = pd.Series(df['거래량'].str.replace(',', '')).astype(int)


#
# print(df.columns)
print(df[df['날짜'] == '2017-03-24']['종가'])

# print(df.irow(0)['시가'])



