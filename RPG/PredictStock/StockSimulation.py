#-*- coding:utf-8 -*-

import pandas as pd
import csv

df = pd.read_csv('data/카카오(035720)_20170626012824.csv')


startDate = pd.to_datetime(df['datetime'].tail(1))
endDate = pd.to_datetime(df['datetime'].head(1))

# print(startDate)
# print(endDate)

periodLimit = 40

# print(df[df['datetime'] > '2017-01-01'])
# print(df[df['datetime'] > '2017-01-01'].__len__())


for i in range(df.__len__()-1, 0, -1):
    profitRate = 0
    maxProfitRate = -1
    # print(i)
    startBuyDate = df['datetime'][i]
    initPrice = df['close'][i]

    for j in range(0, periodLimit):
        if j == 0 :
            continue
            # print(i)
        elif i-j >= 0:
            profitRate = (df['close'][i-j] - initPrice) / initPrice
            if(profitRate > maxProfitRate):
                maxProfitRate = profitRate
        else:
            break

        j += 1

    print(startBuyDate, '에 투자를 시작하면 최대 수익률은 ', maxProfitRate)


# for index, row in data.iterrows():
#     print(index)
#     print(row)

# for i in range(data.count(), 10):
#     print(data.iloc[i])