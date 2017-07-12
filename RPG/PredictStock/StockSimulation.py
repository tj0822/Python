#-*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# stockFileName = '카카오_19991111~20170626'
# stockFileName = '하이닉스_19961226~20170629'
# stockFileName = 'SK이노베이션_20070725~20170627'
stockFileName = '연우_20151102~20170630'


df = pd.read_csv('data/' + stockFileName + '.csv')

startDate = pd.to_datetime(df['datetime'].tail(1))
endDate = pd.to_datetime(df['datetime'].head(1))

# print(startDate)
# print(endDate)

periodLimit = 80

# print(df[df['datetime'] > '2017-01-01'])
# print(df[df['datetime'] > '2017-01-01'].__len__())


outputFileName = 'output/' + stockFileName + '(' + str(periodLimit) + ')' + '.csv'


startBuyDateList = []
initPriceList = []
maxPriceList = []
maxProfitRateList = []
minProfitRateList = []

for i in range(df.__len__()-1, 0, -1):
    profitRate = 0
    maxProfitRate = -999
    minProfitRate = 999
    # print(i)
    startBuyDate = df['datetime'][i]
    initPrice = df['close'][i]
    maxPrice = initPrice
    for j in range(0, periodLimit):
        if j == 0 :
            continue
            # print(i)
        elif i-j >= 0:
            profitRate = (df['close'][i-j] - initPrice) / initPrice
            if(profitRate > maxProfitRate):
                maxProfitRate = profitRate
                maxPrice = df['close'][i-j]

            if(profitRate < minProfitRate):
                minProfitRate = profitRate
        else:
            break

        j += 1

    # print(startBuyDate, '에 투자를 시작하면 최대 수익률은 ', maxProfitRate)
    startBuyDateList.append(startBuyDate)
    initPriceList.append(initPrice)
    maxPriceList.append(maxPrice)
    maxProfitRateList.append(maxProfitRate)
    minProfitRateList.append(minProfitRate)

    # cw.writerow([periodLimit, startBuyDate, initPrice, maxPrice, maxProfitRate, minProfitRate])
df = pd.DataFrame({"startBuyDate": startBuyDateList, "initPrice": initPriceList, "maxPrice": maxPriceList, "maxProfitRate": maxProfitRateList,"minProfitRate": minProfitRateList})


df.to_csv(outputFileName, index = False)

# for index, row in data.iterrows():
#     print(index)
#     print(row)

# for i in range(data.count(), 10):
#     print(data.iloc[i])