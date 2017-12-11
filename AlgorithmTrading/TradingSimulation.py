#-*- coding:utf-8 -*-

import pandas as pd
from os import listdir
from os.path import isfile, join
import datetime

stockDirectory = 'data/2017-11-04/'

result = pd.read_csv('output_2017-12-10_A3.csv', dtype={'종목코드': str}).sort(['날짜'])

totalValue = 0

unitPrice = 1000000     #주식거래 단위 금액
currentValue = 0

portfolio = dict()
fromSimulDate = datetime.datetime.strptime(str(2015) + '-01-01', "%Y-%m-%d").date()
toSimulDate = datetime.datetime.strptime((str(2016) + '-01-01'), "%Y-%m-%d").date()

# result[result[datetime.datetime.strptime(result['날짜'], "%Y-%m-%d").date()] <= toSimulDate]
lastTradeDate = max(result['날짜'])

print(lastTradeDate)

for i in range(0, result.__len__()):
    date = result['날짜'][i]
    sellOrBuy = result['거래유형'][i]
    stockCode = result['종목코드'][i]
    stockName = result['종목명'][i]
    tradePrice = result['거래가격'][i]

    if sellOrBuy == 'buy':
        # 매수
        stockCount = int(unitPrice / tradePrice)
        portfolio[stockCode] = stockCount
        currentValue -= stockCount * tradePrice
        # print(currentCashValue)
        # print(portfolio)
    elif sellOrBuy == 'sell':
        # 매도
        stockCount = portfolio[stockCode]
        del portfolio[stockCode]
        currentValue += stockCount * tradePrice
        # print(currentCashValue)
        # print(portfolio)

    for key, value in portfolio.items():
        stockFiles = (f for f in listdir(stockDirectory) if isfile(join(stockDirectory, f)))
        for fileName in stockFiles:
            if fileName.split('_')[0] == key:
                portfolioStock = pd.read_csv(stockDirectory + fileName)
                currentValue += int(portfolioStock[portfolioStock['datetime'] == date]['close']) * value
                print(currentValue)

# else:
#     for key, value in portfolio.items():
#         stockFiles = (f for f in listdir(stockDirectory) if isfile(join(stockDirectory, f)))
#         for fileName in stockFiles:
#             if fileName.split('_')[0] == key:
#                 portfolioStock = pd.read_csv(stockDirectory + fileName)
#                 currentValue += int(portfolioStock[portfolioStock['datetime'] == lastTradeDate]['close']) * value
#                 print(currentValue)



